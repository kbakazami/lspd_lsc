import { ActionError, defineAction } from 'astro:actions';
import { getRecruitmentSettings } from '@/lib/sanity';
import { z } from 'astro:schema';

/**
 * Discord tronque la valeur d'un champ d'embed à 1024 caractères.
 * On borne les champs libres en deçà pour qu'aucun dossier n'arrive
 * coupé par des points de suspension côté Ressources Humaines.
 */
export const CHAMP_LIBRE_MAX = 1000;

const candidatureSchema = z
  .object({
    nom: z.string().min(2, 'Le nom est requis').max(50),
    prenom: z.string().min(2, 'Le prénom est requis').max(50),
    age: z.coerce.number({ message: 'L\'âge doit être un nombre' })
      .int()
      .min(18, 'Vous devez avoir au moins 18 ans')
      .max(99),
    telephone: z
      .string()
      .trim()
      .min(4, 'Le numéro de téléphone est requis')
      .max(20, 'Le numéro de téléphone est trop long')
      .regex(/^[0-9+().\-\s]+$/, 'Numéro de téléphone invalide'),
    experience: z.enum(['oui', 'non'] as const, {
      message: 'Veuillez indiquer si vous avez une expérience RP',
    }),
    experienceDetails: z
      .string()
      .max(
        CHAMP_LIBRE_MAX,
        `Le détail des expériences ne doit pas dépasser ${CHAMP_LIBRE_MAX} caractères`,
      )
      .optional(),
    motivation: z
      .string()
      .min(80, 'La lettre de motivation doit comporter au moins 80 caractères')
      .max(
        CHAMP_LIBRE_MAX,
        `La lettre de motivation ne doit pas dépasser ${CHAMP_LIBRE_MAX} caractères`,
      ),
    objectifs: z
      .string()
      .min(40, 'Les objectifs doivent comporter au moins 40 caractères')
      .max(
        CHAMP_LIBRE_MAX,
        `Les objectifs ne doivent pas dépasser ${CHAMP_LIBRE_MAX} caractères`,
      ),
  })
  .refine(
    (data) =>
      data.experience === 'non' ||
      (data.experienceDetails != null && data.experienceDetails.trim().length > 0),
    {
      message: 'Veuillez préciser vos expériences RP antérieures',
      path: ['experienceDetails'],
    },
  );

export const server = {
  candidature: defineAction({
    accept: 'form',
    input: candidatureSchema,
    handler: async (data) => {
      // Garde-fou : le formulaire est retiré de la page quand le recrutement est
      // fermé, mais rien n'empêche un POST direct sur l'action.
      const recruitment = await getRecruitmentSettings();
      if (!recruitment.isOpen) {
        throw new ActionError({
          code: 'FORBIDDEN',
          message: 'Le recrutement est actuellement fermé — aucun dossier ne peut être déposé.',
        });
      }

      const webhookUrl = import.meta.env.DISCORD_WEBHOOK_RECRUTEMENT;

      if (!webhookUrl) {
        console.warn('[candidature] DISCORD_WEBHOOK_RECRUTEMENT non configuré — soumission ignorée');
        return { ok: true as const };
      }

      const siteUrl = import.meta.env.PUBLIC_SITE_URL ?? 'https://lspd-lsc.vercel.app';
      const sealUrl = `${siteUrl}/lspd-seal.webp`;

      const trunc = (str: string, max = 1024) =>
        str.length > max ? str.slice(0, max - 1) + '…' : str;

      const dateStr = new Date().toLocaleDateString('fr-FR', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
      });

      const fields = [
        { name: 'Nom', value: data.nom, inline: true },
        { name: 'Prénom', value: data.prenom, inline: true },
        { name: 'Âge', value: `${data.age} ans`, inline: true },
        { name: 'Téléphone', value: data.telephone, inline: true },
        {
          name: 'Expérience RP antérieure',
          value: data.experience === 'oui' ? 'Oui' : 'Non',
          inline: true,
        },
        ...(data.experience === 'oui' && data.experienceDetails
          ? [{ name: 'Expériences détaillées', value: trunc(data.experienceDetails) }]
          : []),
        { name: 'Lettre de motivation', value: trunc(data.motivation) },
        { name: 'Objectifs au sein du LSPD', value: trunc(data.objectifs) },
      ];

      const payload = {
        username: 'LSPD — Ressources Humaines',
        avatar_url: sealUrl,
        embeds: [
          {
            author: {
              name: 'LOS SANTOS POLICE DEPARTMENT',
              icon_url: sealUrl,
            },
            title: `Dossier de candidature — ${data.prenom} ${data.nom}`,
            description: `Un nouveau dossier a été déposé auprès du Bureau des Ressources Humaines.\n**Date de réception :** ${dateStr}`,
            color: 0xc9a961,
            thumbnail: { url: sealUrl },
            fields,
            footer: {
              text: 'Bureau des Ressources Humaines • lspd-lsc.vercel.app',
              icon_url: sealUrl,
            },
            timestamp: new Date().toISOString(),
          },
        ],
      };

      const res = await fetch(webhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      if (!res.ok) {
        throw new Error(`Discord webhook error: ${res.status}`);
      }

      return { ok: true as const };
    },
  }),
};
