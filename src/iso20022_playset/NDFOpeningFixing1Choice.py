import base_types
import Max35Text
import OpeningConditions1

class NDFOpeningFixing1Choice(base_types._BaseFieldType):

	__slots__ = ["_OpngConds", "_OpngConfRef"]
	@property
	def OpngConds(self):
		return self._OpngConds

	@OpngConds.setter
	def OpngConds(self, value):
		self._OpngConds = value if type(value) != auto else self.make_default("OpngConds")

	@OpngConds.deleter
	def OpngConds(self):
		del self._OpngConds
		self._OpngConds = None

	@property
	def OpngConfRef(self):
		return self._OpngConfRef

	@OpngConfRef.setter
	def OpngConfRef(self, value):
		self._OpngConfRef = value if type(value) != auto else self.make_default("OpngConfRef")

	@OpngConfRef.deleter
	def OpngConfRef(self):
		del self._OpngConfRef
		self._OpngConfRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OpngConds', type=OpeningConditions1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OpngConfRef', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

