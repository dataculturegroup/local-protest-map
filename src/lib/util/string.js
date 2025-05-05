import { dateStrForDisplay } from "./date";

export function trimToLength(str, length) {
  if (!str) {
    return "";
  }
  if (str.length > length) {
    return str.substring(0, length) + '...';
  }
  return str;
}

export function autoTitle(mapSettings) {
  if (mapSettings.includeTitle === false) return null;
  let t = "Protests ";
  if (mapSettings.stateId) {
    t += `in ${mapSettings.stateId} `;
  } else {
    t += `within ${mapSettings.radius} miles `;
  }
  t += `between ${dateStrForDisplay(mapSettings.startDate)} and ${dateStrForDisplay(mapSettings.endDate)}`;
  return t;
}
