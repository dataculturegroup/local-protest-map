
// interpret the date from the user in browser local timezone
export const userDateStrToDate = (dateStr) => {
  const [year, month, day] = dateStr.split("-").map(Number);
  return new Date(year, month - 1, day);
};

export const userDateStrToDisplay = (dateStr) => 
  userDateStrToDate(dateStr).toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
