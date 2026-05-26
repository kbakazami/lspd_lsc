import { defineField, defineType } from 'sanity';

export default defineType({
  name: 'recruitmentEvent',
  title: 'Événement de recrutement',
  type: 'document',
  fields: [
    defineField({
      name: 'title',
      title: 'Titre',
      type: 'string',
      validation: (Rule) => Rule.required().max(120),
    }),
    defineField({
      name: 'date',
      title: 'Date et heure de début',
      type: 'datetime',
      options: { timeStep: 15 },
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'endDate',
      title: 'Date et heure de fin (optionnel)',
      type: 'datetime',
      options: { timeStep: 15 },
    }),
    defineField({
      name: 'location',
      title: 'Lieu (IC)',
      type: 'string',
      description: 'Ex. : Commissariat central — Mission Row',
      validation: (Rule) => Rule.required().max(100),
    }),
    defineField({
      name: 'slots',
      title: 'Nombre de places (optionnel)',
      type: 'number',
      validation: (Rule) => Rule.min(1).integer(),
    }),
    defineField({
      name: 'description',
      title: 'Description (optionnel)',
      type: 'text',
      rows: 4,
    }),
    defineField({
      name: 'status',
      title: 'Statut',
      type: 'string',
      options: {
        list: [
          { title: 'Ouvert', value: 'ouvert' },
          { title: 'Complet', value: 'complet' },
          { title: 'Annulé', value: 'annulé' },
        ],
        layout: 'radio',
      },
      initialValue: 'ouvert',
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'discordEventUrl',
      title: 'Lien événement Discord (optionnel)',
      type: 'url',
    }),
  ],
  orderings: [
    {
      title: 'Date croissante',
      name: 'dateAsc',
      by: [{ field: 'date', direction: 'asc' }],
    },
  ],
  preview: {
    select: {
      title: 'title',
      subtitle: 'date',
      status: 'status',
    },
    prepare({ title, subtitle, status }) {
      const icon = status === 'ouvert' ? '✓' : status === 'complet' ? '●' : '✕';
      return { title: `${icon} ${title}`, subtitle };
    },
  },
});
