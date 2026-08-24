import { defineField, defineType } from 'sanity';

export default defineType({
  name: 'recruitmentSettings',
  title: 'Paramètres du recrutement',
  type: 'document',
  fields: [
    defineField({
      name: 'isOpen',
      title: 'Recrutement ouvert',
      type: 'boolean',
      description:
        'Décochez pour fermer le recrutement : le formulaire de candidature est retiré du site et remplacé par le message ci-dessous.',
      initialValue: true,
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'closedTitle',
      title: 'Titre affiché lorsque le recrutement est fermé',
      type: 'string',
      initialValue: 'Recrutement suspendu',
      validation: (Rule) => Rule.max(80),
    }),
    defineField({
      name: 'closedMessage',
      title: 'Message affiché lorsque le recrutement est fermé',
      type: 'text',
      rows: 5,
      initialValue:
        "Le Bureau des Ressources Humaines n'accepte aucun nouveau dossier de candidature pour le moment. Les prochaines sessions de recrutement seront annoncées dans les actualités du département.",
      validation: (Rule) => Rule.max(600),
    }),
    defineField({
      name: 'reopenDate',
      title: 'Réouverture prévue (optionnel)',
      type: 'datetime',
      options: { timeStep: 15 },
      description: 'Si renseignée, la date est affichée sous le message de fermeture.',
    }),
  ],
  preview: {
    select: { isOpen: 'isOpen' },
    prepare({ isOpen }) {
      return {
        title: 'Paramètres du recrutement',
        subtitle: isOpen === false ? '✕ Recrutement fermé' : '✓ Recrutement ouvert',
      };
    },
  },
});
