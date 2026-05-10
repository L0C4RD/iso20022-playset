from . import base_types
from ._Max35Text import Max35Text

class MatchingSystemReference1Choice(base_types._BaseFieldType):

	__slots__ = ["_MtchgSysUnqRef", "_RltdRef"]
	@property
	def MtchgSysUnqRef(self):
		return self._MtchgSysUnqRef

	@MtchgSysUnqRef.setter
	def MtchgSysUnqRef(self, value):
		self._MtchgSysUnqRef = value if type(value) != base_types.auto else self.make_default("MtchgSysUnqRef")

	@MtchgSysUnqRef.deleter
	def MtchgSysUnqRef(self):
		del self._MtchgSysUnqRef
		self._MtchgSysUnqRef = None

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != base_types.auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtchgSysUnqRef', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RltdRef', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

