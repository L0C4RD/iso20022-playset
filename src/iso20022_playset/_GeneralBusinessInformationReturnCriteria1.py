# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestedIndicator

class GeneralBusinessInformationReturnCriteria1(base_types._BaseFieldType):

	__slots__ = ["_QlfrInd", "_SbjtDtlsInd", "_SbjtInd"]
	@property
	def QlfrInd(self):
		return self._QlfrInd

	@QlfrInd.setter
	def QlfrInd(self, value):
		self._QlfrInd = value if value is not None else base_types.UninitialisedField(self, 'QlfrInd', RequestedIndicator, False)

	@QlfrInd.deleter
	def QlfrInd(self):
		del self._QlfrInd
		self._QlfrInd = base_types.UninitialisedField(self, 'QlfrInd', RequestedIndicator, False)

	@property
	def SbjtDtlsInd(self):
		return self._SbjtDtlsInd

	@SbjtDtlsInd.setter
	def SbjtDtlsInd(self, value):
		self._SbjtDtlsInd = value if value is not None else base_types.UninitialisedField(self, 'SbjtDtlsInd', RequestedIndicator, False)

	@SbjtDtlsInd.deleter
	def SbjtDtlsInd(self):
		del self._SbjtDtlsInd
		self._SbjtDtlsInd = base_types.UninitialisedField(self, 'SbjtDtlsInd', RequestedIndicator, False)

	@property
	def SbjtInd(self):
		return self._SbjtInd

	@SbjtInd.setter
	def SbjtInd(self, value):
		self._SbjtInd = value if value is not None else base_types.UninitialisedField(self, 'SbjtInd', RequestedIndicator, False)

	@SbjtInd.deleter
	def SbjtInd(self):
		del self._SbjtInd
		self._SbjtInd = base_types.UninitialisedField(self, 'SbjtInd', RequestedIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QlfrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbjtDtlsInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbjtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))