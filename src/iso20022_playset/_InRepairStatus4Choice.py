from . import base_types
from ._GenericIdentification1 import GenericIdentification1
from ._Max350Text import Max350Text
from ._NoReasonCode import NoReasonCode

class InRepairStatus4Choice(base_types._BaseFieldType):

	__slots__ = ["_Rsn", "_NoSpcfdRsn", "_DataSrcSchme"]
	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def NoSpcfdRsn(self):
		return self._NoSpcfdRsn

	@NoSpcfdRsn.setter
	def NoSpcfdRsn(self, value):
		self._NoSpcfdRsn = value if type(value) != base_types.auto else self.make_default("NoSpcfdRsn")

	@NoSpcfdRsn.deleter
	def NoSpcfdRsn(self):
		del self._NoSpcfdRsn
		self._NoSpcfdRsn = None

	@property
	def DataSrcSchme(self):
		return self._DataSrcSchme

	@DataSrcSchme.setter
	def DataSrcSchme(self, value):
		self._DataSrcSchme = value if type(value) != base_types.auto else self.make_default("DataSrcSchme")

	@DataSrcSchme.deleter
	def DataSrcSchme(self):
		del self._DataSrcSchme
		self._DataSrcSchme = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rsn', type=Max350Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NoSpcfdRsn', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DataSrcSchme', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
	))

