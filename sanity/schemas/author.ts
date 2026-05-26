import { defineField, defineType } from 'sanity';

export default defineType({
  name: 'author',
  title: 'Officier rédacteur',
  type: 'document',
  fields: [
    defineField({
      name: 'name',
      title: 'Nom complet (IC)',
      type: 'string',
      validation: (Rule) => Rule.required().max(80),
    }),
    defineField({
      name: 'rank',
      title: 'Grade',
      type: 'string',
      description: 'Ex. : Sergent, Lieutenant, Inspecteur',
      validation: (Rule) => Rule.required().max(60),
    }),
    defineField({
      name: 'avatar',
      title: 'Photo de profil',
      type: 'image',
      options: { hotspot: true },
    }),
    defineField({
      name: 'bio',
      title: 'Biographie courte',
      type: 'text',
      rows: 3,
      validation: (Rule) => Rule.max(300),
    }),
  ],
  preview: {
    select: {
      title: 'name',
      subtitle: 'rank',
      media: 'avatar',
    },
  },
});
