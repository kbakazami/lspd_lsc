import { defineField, defineType } from 'sanity';

export default defineType({
  name: 'division',
  title: 'Division',
  type: 'document',
  fields: [
    defineField({
      name: 'name',
      title: 'Nom de la division',
      type: 'string',
      validation: (Rule) => Rule.required().max(100),
    }),
    defineField({
      name: 'slug',
      title: 'Slug URL',
      type: 'slug',
      options: { source: 'name' },
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'abbreviation',
      title: 'Sigle',
      type: 'string',
      validation: (Rule) => Rule.required().max(10),
    }),
    defineField({
      name: 'excerpt',
      title: 'Description courte',
      type: 'text',
      rows: 2,
      description: 'Affiché dans les listes et cartes — 1 à 2 phrases max.',
      validation: (Rule) => Rule.max(300),
    }),
    defineField({
      name: 'body',
      title: 'Contenu',
      type: 'array',
      of: [
        { type: 'block' },
        {
          type: 'image',
          options: { hotspot: true },
          fields: [
            defineField({
              name: 'alt',
              title: 'Texte alternatif',
              type: 'string',
              validation: (Rule) => Rule.required(),
            }),
            defineField({
              name: 'caption',
              title: 'Légende',
              type: 'string',
            }),
          ],
        },
      ],
    }),
    defineField({
      name: 'lead',
      title: 'Commandant de division',
      type: 'reference',
      to: [{ type: 'author' }],
    }),
    defineField({
      name: 'members',
      title: 'Membres',
      type: 'array',
      of: [{ type: 'reference', to: [{ type: 'author' }] }],
    }),
    defineField({
      name: 'coverImage',
      title: 'Image de couverture',
      type: 'image',
      options: { hotspot: true },
    }),
    defineField({
      name: 'minRankLevel',
      title: 'Niveau de grade minimum requis',
      type: 'number',
      description: 'Niveau minimal pour postuler à cette division (1–9)',
      validation: (Rule) => Rule.min(1).max(20).integer(),
    }),
  ],
  preview: {
    select: {
      title: 'name',
      subtitle: 'abbreviation',
      media: 'coverImage',
    },
  },
});
