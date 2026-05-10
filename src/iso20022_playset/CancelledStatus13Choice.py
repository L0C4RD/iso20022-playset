from . import base_types
import GenericIdentification1
import NoReasonCode
import CancelledStatusReason3Code
import Extended350Code

class CancelledStatus13Choice(base_types._BaseFieldType):

	__slots__ = ["_DataSrcSchme", "_NoSpcfdRsn", "_XtndedRsn", "_Rsn"]
	@property
	def DataSrcSchme(self):
		return self._DataSrcSchme

	@DataSrcSchme.setter
	def DataSrcSchme(self, value):
		self._DataSrcSchme = value if type(value) != auto else self.make_default("DataSrcSchme")

	@DataSrcSchme.deleter
	def DataSrcSchme(self):
		del self._DataSrcSchme
		self._DataSrcSchme = None

	@property
	def NoSpcfdRsn(self):
		return self._NoSpcfdRsn

	@NoSpcfdRsn.setter
	def NoSpcfdRsn(self, value):
		self._NoSpcfdRsn = value if type(value) != auto else self.make_default("NoSpcfdRsn")

	@NoSpcfdRsn.deleter
	def NoSpcfdRsn(self):
		del self._NoSpcfdRsn
		self._NoSpcfdRsn = None

	@property
	def XtndedRsn(self):
		return self._XtndedRsn

	@XtndedRsn.setter
	def XtndedRsn(self, value):
		self._XtndedRsn = value if type(value) != auto else self.make_default("XtndedRsn")

	@XtndedRsn.deleter
	def XtndedRsn(self):
		del self._XtndedRsn
		self._XtndedRsn = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSrcSchme', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NoSpcfdRsn', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XtndedRsn', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rsn', type=CancelledStatusReason3Code, min=0, max=1, mutex_group=1, array=False),
	))

