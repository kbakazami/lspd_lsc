import { createClient } from '@sanity/client';

// ─── Posts (Actualités) ──────────────────────────────────────────────────────

export interface SanityAuthorRef {
  name: string;
  rank: string;
}

export interface SanityBodySpan {
  _type: 'span';
  text: string;
  marks?: string[];
}

export interface SanityBodyBlock {
  _type: 'block';
  style?: string;
  children: SanityBodySpan[];
  markDefs?: Array<{ _key: string; _type: string; href?: string }>;
}

export interface SanityBodyImage {
  _type: 'image';
  url?: string;
  alt?: string;
  caption?: string;
}

export type SanityBodyContent = SanityBodyBlock | SanityBodyImage;

export interface SanityPost {
  _id: string;
  title: string;
  slug: { current: string };
  publishedAt: string;
  author: SanityAuthorRef;
  excerpt: string;
  coverImage?: { url: string; alt?: string };
  body?: SanityBodyContent[];
  tags?: string[];
}

// ─── Organigramme ─────────────────────────────────────────────────────────────

export type RankTier = 'direction' | 'commandStaff' | 'supervision' | 'personnel';

export interface SanityRank {
  _id: string;
  name: string;
  abbreviation: string;
  tier: RankTier;
  level: number;
  badge?: { url: string };
  description?: string;
}

export interface SanityDivisionLead {
  name: string;
  rank: string;
}

export interface SanityDivisionMember {
  name: string;
  rank: string;
  avatar?: { url: string };
}

export type DivisionType = 'majeure' | 'mineure';

export interface SanityDivision {
  _id: string;
  name: string;
  slug: { current: string };
  abbreviation: string;
  excerpt?: string;
  lead?: SanityDivisionLead;
  memberCount: number;
  divisionType?: DivisionType;
  minRankLevel?: number;
  coverImage?: { url: string; alt?: string };
}

export interface SanityDivisionDetail {
  _id: string;
  name: string;
  slug: { current: string };
  abbreviation: string;
  excerpt?: string;
  body?: SanityBodyContent[];
  lead?: SanityDivisionLead;
  members?: SanityDivisionMember[];
  memberCount: number;
  divisionType?: DivisionType;
  minRankLevel?: number;
  coverImage?: { url: string; alt?: string };
}

// ─── Recrutement ─────────────────────────────────────────────────────────────

export type RecruitmentEventStatus = 'ouvert' | 'complet' | 'annulé';

export interface RecruitmentEvent {
  _id: string;
  title: string;
  date: string;
  endDate: string | null;
  location: string;
  slots: number | null;
  description: string | null;
  status: RecruitmentEventStatus;
  discordEventUrl: string | null;
}

export interface RecruitmentSettings {
  isOpen: boolean;
  closedTitle: string;
  closedMessage: string;
  reopenDate: string | null;
}

/** Valeurs retenues tant qu'aucun document n'existe dans Sanity. */
export const DEFAULT_RECRUITMENT_SETTINGS: RecruitmentSettings = {
  isOpen: true,
  closedTitle: 'Recrutement suspendu',
  closedMessage:
    "Le Bureau des Ressources Humaines n'accepte aucun nouveau dossier de candidature pour le moment. Les prochaines sessions de recrutement seront annoncées dans les actualités du département.",
  reopenDate: null,
};

function createSanityClient() {
  const projectId = import.meta.env.PUBLIC_SANITY_PROJECT_ID;
  const dataset = import.meta.env.PUBLIC_SANITY_DATASET ?? 'production';
  const token = import.meta.env.SANITY_API_READ_TOKEN;

  if (!projectId) {
    return null;
  }

  return createClient({
    projectId,
    dataset,
    apiVersion: '2026-05-20',
    useCdn: false,
    token: token ?? undefined,
  });
}

const UPCOMING_EVENTS_QUERY = `
  *[
    _type == "recruitmentEvent" &&
    date >= $from &&
    date <= $to
  ] | order(date asc) {
    _id,
    title,
    date,
    endDate,
    location,
    slots,
    description,
    status,
    discordEventUrl
  }
`;

const RECRUITMENT_SETTINGS_QUERY = `
  *[_type == "recruitmentSettings"][0] {
    isOpen,
    closedTitle,
    closedMessage,
    reopenDate
  }
`;

const ALL_POSTS_QUERY = `
  *[_type == "post"] | order(publishedAt desc) {
    _id,
    title,
    slug,
    publishedAt,
    "author": author->{ name, rank },
    excerpt,
    "coverImage": coverImage{ "url": asset->url, alt },
    tags
  }
`;

const POST_BY_SLUG_QUERY = `
  *[_type == "post" && slug.current == $slug][0] {
    _id,
    title,
    slug,
    publishedAt,
    "author": author->{ name, rank },
    excerpt,
    "coverImage": coverImage{ "url": asset->url, alt },
    "body": body[]{
      ...,
      _type == "image" => {
        "url": asset->url,
        alt,
        caption
      }
    },
    tags
  }
`;

const ALL_RANKS_QUERY = `
  *[_type == "rank"] | order(level desc) {
    _id,
    name,
    abbreviation,
    tier,
    level,
    "badge": badge{ "url": asset->url },
    description
  }
`;

const ALL_DIVISIONS_QUERY = `
  *[_type == "division"] | order(name asc) {
    _id,
    name,
    slug,
    abbreviation,
    excerpt,
    "lead": lead->{ name, rank },
    "memberCount": count(members),
    divisionType,
    minRankLevel,
    "coverImage": coverImage{ "url": asset->url, alt }
  }
`;

const DIVISION_BY_SLUG_QUERY = `
  *[_type == "division" && slug.current == $slug][0] {
    _id,
    name,
    slug,
    abbreviation,
    excerpt,
    "body": body[]{
      ...,
      _type == "image" => {
        "url": asset->url,
        alt,
        caption
      }
    },
    "lead": lead->{ name, rank },
    "members": members[]->{ name, rank, "avatar": avatar{ "url": asset->url } },
    "memberCount": count(members),
    divisionType,
    minRankLevel,
    "coverImage": coverImage{ "url": asset->url, alt }
  }
`;

export async function getAllRanks(): Promise<SanityRank[]> {
  const client = createSanityClient();
  if (!client) {
    console.warn('[sanity] PUBLIC_SANITY_PROJECT_ID non configuré — aucun grade chargé');
    return [];
  }
  try {
    return await client.fetch<SanityRank[]>(ALL_RANKS_QUERY);
  } catch (err) {
    console.error('[sanity] Erreur lors du chargement des grades :', err);
    return [];
  }
}

export async function getAllDivisions(): Promise<SanityDivision[]> {
  const client = createSanityClient();
  if (!client) {
    console.warn('[sanity] PUBLIC_SANITY_PROJECT_ID non configuré — aucune division chargée');
    return [];
  }
  try {
    return await client.fetch<SanityDivision[]>(ALL_DIVISIONS_QUERY);
  } catch (err) {
    console.error('[sanity] Erreur lors du chargement des divisions :', err);
    return [];
  }
}

export async function getDivisionBySlug(slug: string): Promise<SanityDivisionDetail | null> {
  const client = createSanityClient();
  if (!client) return null;
  try {
    return await client.fetch<SanityDivisionDetail | null>(DIVISION_BY_SLUG_QUERY, { slug });
  } catch (err) {
    console.error('[sanity] Erreur lors du chargement de la division :', err);
    return null;
  }
}

export async function getAllPosts(): Promise<SanityPost[]> {
  const client = createSanityClient();
  if (!client) {
    console.warn('[sanity] PUBLIC_SANITY_PROJECT_ID non configuré — aucun article chargé');
    return [];
  }
  try {
    return await client.fetch<SanityPost[]>(ALL_POSTS_QUERY);
  } catch (err) {
    console.error('[sanity] Erreur lors du chargement des articles :', err);
    return [];
  }
}

export async function getPostBySlug(slug: string): Promise<SanityPost | null> {
  const client = createSanityClient();
  if (!client) return null;
  try {
    return await client.fetch<SanityPost | null>(POST_BY_SLUG_QUERY, { slug });
  } catch (err) {
    console.error("[sanity] Erreur lors du chargement de l'article :", err);
    return null;
  }
}

export async function getUpcomingRecruitmentEvents(): Promise<RecruitmentEvent[]> {
  const client = createSanityClient();

  if (!client) {
    console.warn('[sanity] PUBLIC_SANITY_PROJECT_ID non configuré — aucun événement chargé');
    return [];
  }

  const now = new Date();
  const sixMonthsLater = new Date(now);
  sixMonthsLater.setMonth(sixMonthsLater.getMonth() + 6);

  try {
    return await client.fetch<RecruitmentEvent[]>(UPCOMING_EVENTS_QUERY, {
      from: now.toISOString(),
      to: sixMonthsLater.toISOString(),
    });
  } catch (err) {
    console.error('[sanity] Erreur lors du chargement des événements de recrutement :', err);
    return [];
  }
}

export async function getRecruitmentSettings(): Promise<RecruitmentSettings> {
  const client = createSanityClient();

  if (!client) {
    console.warn('[sanity] PUBLIC_SANITY_PROJECT_ID non configuré — recrutement considéré ouvert');
    return DEFAULT_RECRUITMENT_SETTINGS;
  }

  try {
    const doc = await client.fetch<Partial<RecruitmentSettings> | null>(
      RECRUITMENT_SETTINGS_QUERY,
    );

    if (!doc) return DEFAULT_RECRUITMENT_SETTINGS;

    return {
      isOpen: doc.isOpen !== false,
      closedTitle: doc.closedTitle || DEFAULT_RECRUITMENT_SETTINGS.closedTitle,
      closedMessage: doc.closedMessage || DEFAULT_RECRUITMENT_SETTINGS.closedMessage,
      reopenDate: doc.reopenDate ?? null,
    };
  } catch (err) {
    console.error('[sanity] Erreur lors du chargement des paramètres de recrutement :', err);
    return DEFAULT_RECRUITMENT_SETTINGS;
  }
}
