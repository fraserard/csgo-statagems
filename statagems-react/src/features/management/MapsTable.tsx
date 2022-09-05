import { Table } from "@mantine/core";
import { useState } from "react";
import { ManageMapsFragment } from "~/graphql";
import MapsTableAdd from "./MapsTableAdd";
import MapsTableRow from "./MapsTableRow";

interface MapsTableProps {
  mapsFragment: ManageMapsFragment[];
}

export default function MapsTable({ mapsFragment}: MapsTableProps) {
  const [maps, setMaps] = useState(mapsFragment);

  const addMap = (map: ManageMapsFragment) => (
    setMaps(maps => [...maps, {...map}])
  )
    
  const editMap = (map: ManageMapsFragment) => {
    setMaps((maps) =>
      maps!.map((m) => {
        if (m.id === map.id) {
          return { ...map };
        }
        return m;
      })
    );
  };
  const rows = maps.map((map) => <MapsTableRow key={map.id} map={map} editMap={editMap} />);
  return (
    <Table>
      <thead>
        <tr>
          <th>Filename</th>
          <th>Map Name</th>
          <th>Active Duty</th>
          <th>Removed</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <MapsTableAdd addMap={addMap}/>
        {rows}
      </tbody>
    </Table>
  );
}
