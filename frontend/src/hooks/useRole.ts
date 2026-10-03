import { useEffect, useState } from 'react';

export type UserRole = 'doctor' | 'researcher' | 'admin' | 'patient';

export const rolePermissions: Record<UserRole, string[]> = {
  doctor: ['patients', 'screening', 'predictions', 'reports', 'appointments'],
  researcher: ['datasets', 'experiments', 'ml', 'qml', 'benchmarking', 'robustness', 'fairness'],
  admin: ['users', 'permissions', 'audit', 'settings'],
  patient: ['screening', 'results', 'history', 'reports'],
};

export function useRole(role: UserRole) {
  const [permissions, setPermissions] = useState<string[]>([]);

  useEffect(() => {
    setPermissions(rolePermissions[role]);
  }, [role]);

  return permissions;
}
