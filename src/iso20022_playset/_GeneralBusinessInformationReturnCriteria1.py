from . import base_types
from ._RequestedIndicator import RequestedIndicator

class GeneralBusinessInformationReturnCriteria1(base_types._BaseFieldType):

	__slots__ = ["_SbjtInd", "_SbjtDtlsInd", "_QlfrInd"]
	@property
	def SbjtInd(self):
		return self._SbjtInd

	@SbjtInd.setter
	def SbjtInd(self, value):
		self._SbjtInd = value if type(value) != base_types.auto else self.make_default("SbjtInd")

	@SbjtInd.deleter
	def SbjtInd(self):
		del self._SbjtInd
		self._SbjtInd = None

	@property
	def SbjtDtlsInd(self):
		return self._SbjtDtlsInd

	@SbjtDtlsInd.setter
	def SbjtDtlsInd(self, value):
		self._SbjtDtlsInd = value if type(value) != base_types.auto else self.make_default("SbjtDtlsInd")

	@SbjtDtlsInd.deleter
	def SbjtDtlsInd(self):
		del self._SbjtDtlsInd
		self._SbjtDtlsInd = None

	@property
	def QlfrInd(self):
		return self._QlfrInd

	@QlfrInd.setter
	def QlfrInd(self, value):
		self._QlfrInd = value if type(value) != base_types.auto else self.make_default("QlfrInd")

	@QlfrInd.deleter
	def QlfrInd(self):
		del self._QlfrInd
		self._QlfrInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SbjtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbjtDtlsInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QlfrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

