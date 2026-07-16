# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DetailedAbnormalValuesStatistics4Choice
from . import DetailedMissingMarginInformationStatistics4Choice
from . import DetailedMissingValuationsStatistics4Choice
from . import ISODate

class DetailedStatisticsPerCounterparty17(base_types._BaseFieldType):

	__slots__ = ["_AbnrmlVals", "_MssngMrgnInf", "_MssngValtn", "_RefDt"]
	@property
	def AbnrmlVals(self):
		return self._AbnrmlVals

	@AbnrmlVals.setter
	def AbnrmlVals(self, value):
		self._AbnrmlVals = value if value is not None else base_types.UninitialisedField(self, 'AbnrmlVals', DetailedAbnormalValuesStatistics4Choice, False)

	@AbnrmlVals.deleter
	def AbnrmlVals(self):
		del self._AbnrmlVals
		self._AbnrmlVals = base_types.UninitialisedField(self, 'AbnrmlVals', DetailedAbnormalValuesStatistics4Choice, False)

	@property
	def MssngMrgnInf(self):
		return self._MssngMrgnInf

	@MssngMrgnInf.setter
	def MssngMrgnInf(self, value):
		self._MssngMrgnInf = value if value is not None else base_types.UninitialisedField(self, 'MssngMrgnInf', DetailedMissingMarginInformationStatistics4Choice, False)

	@MssngMrgnInf.deleter
	def MssngMrgnInf(self):
		del self._MssngMrgnInf
		self._MssngMrgnInf = base_types.UninitialisedField(self, 'MssngMrgnInf', DetailedMissingMarginInformationStatistics4Choice, False)

	@property
	def MssngValtn(self):
		return self._MssngValtn

	@MssngValtn.setter
	def MssngValtn(self, value):
		self._MssngValtn = value if value is not None else base_types.UninitialisedField(self, 'MssngValtn', DetailedMissingValuationsStatistics4Choice, False)

	@MssngValtn.deleter
	def MssngValtn(self):
		del self._MssngValtn
		self._MssngValtn = base_types.UninitialisedField(self, 'MssngValtn', DetailedMissingValuationsStatistics4Choice, False)

	@property
	def RefDt(self):
		return self._RefDt

	@RefDt.setter
	def RefDt(self, value):
		self._RefDt = value if value is not None else base_types.UninitialisedField(self, 'RefDt', ISODate, False)

	@RefDt.deleter
	def RefDt(self):
		del self._RefDt
		self._RefDt = base_types.UninitialisedField(self, 'RefDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AbnrmlVals', type=DetailedAbnormalValuesStatistics4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MssngMrgnInf', type=DetailedMissingMarginInformationStatistics4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MssngValtn', type=DetailedMissingValuationsStatistics4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))