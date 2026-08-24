import { defineField, defineType } from 'sanity';

export const RANK_TIERS = [
  { title: 'Direction',              value: 'direction'   },
  { title: 'Command Staff',          value: 'commandStaff'},
  { title: 'Supervision',            value: 'supervision' },
  { title: 'Personnel opérationnel', value: 'personnel'   },
] as const;

export type RankTierValue = (typeof RANK_TIERS)[number]['value'];

export default defineType({
  name: 'rank',
  title: 'Grade',
  type: 'document',
  fields: [
    defineField({
      name: 'name',
      title: 'Intitulé du grade',
      type: 'string',
      validation: (Rule) => Rule.required().max(80),
    }),
    defineField({
      name: 'abbreviation',
      title: 'Abréviation',
      type: 'string',
      validation: (Rule) => Rule.required().max(10),
    }),
    defineField({
      name: 'tier',
      title: 'Catégorie',
      type: 'string',
      options: {
        list: [...RANK_TIERS],
        layout: 'radio',
      },
      validation: (Rule) => Rule.required(),
    }),
    defineField({
      name: 'level',
      title: 'Niveau hiérarchique',
      type: 'number',
      description: 'Ordre d\'affichage au sein de la catégorie — le plus grand chiffre apparaît en tête de liste.',
      validation: (Rule) => Rule.required().min(1).max(20).integer(),
    }),
    defineField({
      name: 'badge',
      title: 'Insigne',
      type: 'image',
      options: { hotspot: true },
    }),
    defineField({
      name: 'description',
      title: 'Description du grade',
      type: 'text',
      rows: 3,
      validation: (Rule) => Rule.max(500),
    }),
  ],
  orderings: [
    {
      title: 'Niveau hiérarchique (haut → bas)',
      name: 'levelDesc',
      by: [{ field: 'level', direction: 'desc' }],
    },
  ],
  preview: {
    select: {
      title: 'name',
      subtitle: 'tier',
      media: 'badge',
    },
    prepare({ title, subtitle, media }) {
      const tier = RANK_TIERS.find(t => t.value === subtitle);
      return { title, subtitle: tier?.title ?? subtitle, media };
    },
  },
});
