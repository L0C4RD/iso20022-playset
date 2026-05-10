import base_types
import NameAndLocation1
import LEIIdentifier
import SectorAndLocation1

class CounterpartyIdentification3Choice(base_types._BaseFieldType):

	__slots__ = ["_LEI", "_NmAndLctn", "_SctrAndLctn"]
	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	@property
	def NmAndLctn(self):
		return self._NmAndLctn

	@NmAndLctn.setter
	def NmAndLctn(self, value):
		self._NmAndLctn = value if type(value) != auto else self.make_default("NmAndLctn")

	@NmAndLctn.deleter
	def NmAndLctn(self):
		del self._NmAndLctn
		self._NmAndLctn = None

	@property
	def SctrAndLctn(self):
		return self._SctrAndLctn

	@SctrAndLctn.setter
	def SctrAndLctn(self, value):
		self._SctrAndLctn = value if type(value) != auto else self.make_default("SctrAndLctn")

	@SctrAndLctn.deleter
	def SctrAndLctn(self):
		del self._SctrAndLctn
		self._SctrAndLctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmAndLctn', type=NameAndLocation1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctrAndLctn', type=SectorAndLocation1, min=0, max=1, mutex_group=1, array=False),
	))

