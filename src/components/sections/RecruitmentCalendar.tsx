import { useState, useCallback } from 'react';
import type { RecruitmentEvent, RecruitmentEventStatus } from '@/lib/sanity';

interface RecruitmentCalendarProps {
  events: RecruitmentEvent[];
  initialYear: number;
  initialMonth: number;
}

interface CalendarDay {
  date: Date;
  isCurrentMonth: boolean;
  isToday: boolean;
  events: RecruitmentEvent[];
}

function buildCalendarGrid(
  year: number,
  month: number,
  events: RecruitmentEvent[]
): CalendarDay[][] {
  const firstOfMonth = new Date(year, month, 1);
  const startOffset = (firstOfMonth.getDay() + 6) % 7;

  const gridStart = new Date(firstOfMonth);
  gridStart.setDate(gridStart.getDate() - startOffset);

  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const eventsByDay = new Map<string, RecruitmentEvent[]>();
  for (const event of events) {
    const d = new Date(event.date);
    const key = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
    const existing = eventsByDay.get(key) ?? [];
    existing.push(event);
    eventsByDay.set(key, existing);
  }

  const weeks: CalendarDay[][] = [];
  const cursor = new Date(gridStart);

  for (let week = 0; week < 6; week++) {
    const days: CalendarDay[] = [];
    for (let dow = 0; dow < 7; dow++) {
      const cellDate = new Date(cursor);
      const key = `${cellDate.getFullYear()}-${String(cellDate.getMonth() + 1).padStart(2, '0')}-${String(cellDate.getDate()).padStart(2, '0')}`;
      days.push({
        date: cellDate,
        isCurrentMonth: cellDate.getMonth() === month,
        isToday: cellDate.getTime() === today.getTime(),
        events: eventsByDay.get(key) ?? [],
      });
      cursor.setDate(cursor.getDate() + 1);
    }
    weeks.push(days);
  }

  return weeks;
}

function formatDateLong(iso: string): string {
  return new Intl.DateTimeFormat('fr-FR', {
    weekday: 'long',
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  }).format(new Date(iso));
}

function formatTimeLong(iso: string): string {
  return new Intl.DateTimeFormat('fr-FR', {
    hour: '2-digit',
    minute: '2-digit',
  }).format(new Date(iso));
}

const STATUS_STYLES: Record<RecruitmentEventStatus, { label: string; classes: string }> = {
  ouvert: {
    label: 'Ouvert',
    classes: 'text-success bg-success/10 border border-success/20',
  },
  complet: {
    label: 'Complet',
    classes: 'text-warning bg-warning/10 border border-warning/20',
  },
  annulé: {
    label: 'Annulé',
    classes: 'text-danger bg-danger/10 border border-danger/20',
  },
};

const STATUS_TEXT: Record<RecruitmentEventStatus, string> = {
  ouvert: 'text-success',
  complet: 'text-warning',
  annulé: 'text-danger/70',
};

const WEEKDAYS = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'];

export default function RecruitmentCalendar({
  events,
  initialYear,
  initialMonth,
}: RecruitmentCalendarProps) {
  const [year, setYear] = useState(initialYear);
  const [month, setMonth] = useState(initialMonth);
  const [selectedEvent, setSelectedEvent] = useState<RecruitmentEvent | null>(null);

  const isInitialMonth = year === initialYear && month === initialMonth;

  const goToPrev = useCallback(() => {
    if (isInitialMonth) return;
    setSelectedEvent(null);
    if (month === 0) {
      setMonth(11);
      setYear((y) => y - 1);
    } else {
      setMonth((m) => m - 1);
    }
  }, [month, year, isInitialMonth]);

  const goToNext = useCallback(() => {
    setSelectedEvent(null);
    if (month === 11) {
      setMonth(0);
      setYear((y) => y + 1);
    } else {
      setMonth((m) => m + 1);
    }
  }, [month]);

  const monthLabel = new Intl.DateTimeFormat('fr-FR', {
    month: 'long',
    year: 'numeric',
  }).format(new Date(year, month, 1));

  const grid = buildCalendarGrid(year, month, events);

  return (
    <div className="flex flex-col lg:flex-row gap-5">

        {/* Calendrier */}
        <div className="flex-1 bg-surface border border-border overflow-hidden" style={{ borderRadius: 'var(--radius-md)' }}>

          {/* Navigation mois */}
          <div className="flex items-center justify-between px-5 py-4 border-b border-border bg-lspd-navy/2">
            <button
              onClick={goToPrev}
              disabled={isInitialMonth}
              aria-label="Mois précédent"
              className="w-8 h-8 flex items-center justify-center border border-border text-text-muted hover:border-lspd-navy hover:text-lspd-navy disabled:opacity-25 disabled:cursor-not-allowed transition-colors"
              style={{ borderRadius: 'var(--radius-sm)' }}
            >
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                <polyline points="15 18 9 12 15 6" />
              </svg>
            </button>

            <span className="font-display font-semibold text-text capitalize text-lg" style={{ letterSpacing: '0.02em' }}>
              {monthLabel}
            </span>

            <button
              onClick={goToNext}
              aria-label="Mois suivant"
              className="w-8 h-8 flex items-center justify-center border border-border text-text-muted hover:border-lspd-navy hover:text-lspd-navy transition-colors"
              style={{ borderRadius: 'var(--radius-sm)' }}
            >
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                <polyline points="9 18 15 12 9 6" />
              </svg>
            </button>
          </div>

          {/* En-tête jours */}
          <div className="grid grid-cols-7 border-b border-border">
            {WEEKDAYS.map((d) => (
              <div key={d} className="text-center text-[10px] font-mono tracking-widest uppercase text-text-subtle py-2.5 border-r border-border/50 last:border-r-0">
                {d}
              </div>
            ))}
          </div>

          {/* Grille */}
          <div>
            {grid.map((week, wi) => (
              <div key={wi} className="grid grid-cols-7 border-b border-border/50 last:border-b-0">
                {week.map((day, di) => {
                  const hasEvents = day.events.length > 0;
                  const isSelected = selectedEvent !== null && day.events.some((e) => e._id === selectedEvent._id);
                  const firstEvent = day.events[0];

                  return (
                    <div
                      key={di}
                      role={hasEvents ? 'button' : undefined}
                      tabIndex={hasEvents ? 0 : undefined}
                      aria-pressed={hasEvents ? isSelected : undefined}
                      onClick={hasEvents ? () => setSelectedEvent(firstEvent ?? null) : undefined}
                      onKeyDown={
                        hasEvents
                          ? (e) => {
                              if (e.key === 'Enter' || e.key === ' ') {
                                e.preventDefault();
                                setSelectedEvent(firstEvent ?? null);
                              }
                            }
                          : undefined
                      }
                      className={[
                        'relative flex flex-col p-1.5 min-h-[72px] border-r border-border/50 last:border-r-0',
                        'transition-colors duration-150',
                        !day.isCurrentMonth ? 'opacity-30' : '',
                        hasEvents && !isSelected
                          ? 'cursor-pointer bg-lspd-navy/[0.03] hover:bg-lspd-navy/[0.07] focus:outline-none focus:bg-lspd-navy/[0.07]'
                          : '',
                        isSelected ? 'bg-lspd-gold/10 cursor-pointer' : '',
                      ].filter(Boolean).join(' ')}
                    >
                      {/* Barre gold en haut des cellules avec événement */}
                      {hasEvents && (
                        <div
                          className={`absolute top-0 left-0 right-0 h-0.5 ${isSelected ? 'bg-lspd-gold' : 'bg-lspd-gold/50'}`}
                        />
                      )}

                      {/* Numéro du jour */}
                      <div className="flex items-start justify-between mb-1">
                        {hasEvents ? (
                          <span
                            className={[
                              'w-6 h-6 flex items-center justify-center text-[11px] font-mono font-semibold leading-none shrink-0',
                              day.isToday
                                ? 'bg-lspd-gold text-lspd-navy-deep'
                                : isSelected
                                  ? 'bg-lspd-navy text-white'
                                  : 'bg-lspd-navy/85 text-white',
                            ].join(' ')}
                            style={{ borderRadius: 'var(--radius-sm)' }}
                          >
                            {day.date.getDate()}
                          </span>
                        ) : (
                          <span
                            className={[
                              'w-6 h-6 flex items-center justify-center text-[11px] font-mono leading-none',
                              day.isToday
                                ? 'bg-lspd-gold/15 text-lspd-navy font-semibold'
                                : 'text-text-subtle',
                            ].join(' ')}
                            style={{ borderRadius: 'var(--radius-sm)' }}
                          >
                            {day.date.getDate()}
                          </span>
                        )}

                        {/* Indicateur multi-événements */}
                        {day.events.length > 1 && (
                          <span className="text-[8px] font-mono text-text-subtle leading-none mt-1">
                            +{day.events.length - 1}
                          </span>
                        )}
                      </div>

                      {/* Titre de l'événement */}
                      {firstEvent && (
                        <div className="flex-1 min-w-0">
                          <p className={`text-[9px] font-mono leading-snug line-clamp-2 ${STATUS_TEXT[firstEvent.status]}`}>
                            {firstEvent.title}
                          </p>
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            ))}
          </div>

          {/* Légende */}
          <div className="px-5 py-3 border-t border-border flex flex-wrap gap-4 bg-bg/40">
            {(Object.entries(STATUS_STYLES) as [RecruitmentEventStatus, { label: string; classes: string }][]).map(
              ([key, { label }]) => (
                <div key={key} className="flex items-center gap-1.5">
                  <span className={`text-[10px] font-mono uppercase tracking-wider ${STATUS_TEXT[key]}`}>●</span>
                  <span className="text-[10px] font-mono text-text-subtle uppercase tracking-wider">{label}</span>
                </div>
              )
            )}
          </div>
        </div>

        {/* Panneau détail */}
        <div className="lg:w-64 xl:w-72">
          {selectedEvent ? (
            <div className="bg-surface border border-border" style={{ borderRadius: 'var(--radius-md)' }}>
              {/* Bandeau statut */}
              <div className={`px-5 py-2.5 border-b ${STATUS_STYLES[selectedEvent.status].classes} flex items-center justify-between`} style={{ borderTopLeftRadius: 'var(--radius-md)', borderTopRightRadius: 'var(--radius-md)' }}>
                <span className="text-[10px] font-mono tracking-widest uppercase font-semibold">
                  {STATUS_STYLES[selectedEvent.status].label}
                </span>
                <button
                  onClick={() => setSelectedEvent(null)}
                  aria-label="Fermer le détail"
                  className="w-5 h-5 flex items-center justify-center opacity-60 hover:opacity-100 transition-opacity"
                >
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
                    <line x1="18" y1="6" x2="6" y2="18" />
                    <line x1="6" y1="6" x2="18" y2="18" />
                  </svg>
                </button>
              </div>

              {/* Titre */}
              <div className="px-5 py-4 border-b border-border">
                <p className="text-[10px] font-mono tracking-[0.25em] uppercase text-text-subtle mb-1">
                  Session de recrutement
                </p>
                <h3 className="font-display font-semibold text-text text-xl leading-snug">
                  {selectedEvent.title}
                </h3>
              </div>

              <div className="px-5 py-5 space-y-4">

                {/* Date — mise en avant */}
                <div className="bg-lspd-navy/4 border border-lspd-gold/20 px-4 py-3" style={{ borderRadius: 'var(--radius-sm)' }}>
                  <p className="text-[10px] font-mono tracking-[0.2em] uppercase text-lspd-gold/70 mb-1">Date</p>
                  <p className="text-sm text-text font-semibold capitalize leading-snug">{formatDateLong(selectedEvent.date)}</p>
                  {selectedEvent.endDate && (
                    <p className="text-xs text-text-muted mt-1">
                      Fin : {formatTimeLong(selectedEvent.endDate)}
                    </p>
                  )}
                </div>

                {/* Lieu */}
                <div className="flex items-start gap-3">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#c9a961" strokeWidth="1.5" strokeLinecap="round" className="shrink-0 mt-0.5 opacity-70">
                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
                    <circle cx="12" cy="10" r="3" />
                  </svg>
                  <div>
                    <p className="text-[10px] font-mono tracking-[0.2em] uppercase text-text-subtle mb-0.5">Lieu</p>
                    <p className="text-sm text-text">{selectedEvent.location}</p>
                  </div>
                </div>

                {/* Places */}
                {selectedEvent.slots !== null && (
                  <div className="flex items-start gap-3">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#c9a961" strokeWidth="1.5" strokeLinecap="round" className="shrink-0 mt-0.5 opacity-70">
                      <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
                      <circle cx="9" cy="7" r="4" />
                      <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
                      <path d="M16 3.13a4 4 0 0 1 0 7.75" />
                    </svg>
                    <div>
                      <p className="text-[10px] font-mono tracking-[0.2em] uppercase text-text-subtle mb-0.5">Places</p>
                      <p className="text-sm text-text">{selectedEvent.slots} place{selectedEvent.slots > 1 ? 's' : ''}</p>
                    </div>
                  </div>
                )}

                {/* Description */}
                {selectedEvent.description && (
                  <div className="pt-1 border-t border-border">
                    <p className="text-[10px] font-mono tracking-[0.2em] uppercase text-text-subtle mb-2">Description</p>
                    <p className="text-sm text-text-muted leading-relaxed whitespace-pre-line">{selectedEvent.description}</p>
                  </div>
                )}

                {/* Lien Discord */}
                {selectedEvent.discordEventUrl && (
                  <a
                    href={selectedEvent.discordEventUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center gap-2 text-xs font-mono text-lspd-navy hover:text-lspd-navy-deep underline underline-offset-2 transition-colors"
                  >
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round">
                      <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
                      <polyline points="15 3 21 3 21 9" />
                      <line x1="10" y1="14" x2="21" y2="3" />
                    </svg>
                    Voir l'événement Discord
                  </a>
                )}
              </div>
            </div>
          ) : (
            <div className="hidden lg:flex bg-surface border border-dashed border-border h-full min-h-[180px] items-center justify-center" style={{ borderRadius: 'var(--radius-md)' }}>
              <p className="text-[10px] font-mono tracking-[0.25em] uppercase text-text-subtle text-center px-6 leading-loose">
                Sélectionnez<br />une session
              </p>
            </div>
          )}
        </div>

      </div>
  );
}
