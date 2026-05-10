from . import base_types
import ISODate
import DetailedAbnormalValuesStatistics4Choice
import DetailedMissingMarginInformationStatistics4Choice
import DetailedMissingValuationsStatistics4Choice

class DetailedStatisticsPerCounterparty17(base_types._BaseFieldType):

	__slots__ = ["_MssngMrgnInf", "_MssngValtn", "_AbnrmlVals", "_RefDt"]
	@property
	def MssngMrgnInf(self):
		return self._MssngMrgnInf

	@MssngMrgnInf.setter
	def MssngMrgnInf(self, value):
		self._MssngMrgnInf = value if type(value) != auto else self.make_default("MssngMrgnInf")

	@MssngMrgnInf.deleter
	def MssngMrgnInf(self):
		del self._MssngMrgnInf
		self._MssngMrgnInf = None

	@property
	def MssngValtn(self):
		return self._MssngValtn

	@MssngValtn.setter
	def MssngValtn(self, value):
		self._MssngValtn = value if type(value) != auto else self.make_default("MssngValtn")

	@MssngValtn.deleter
	def MssngValtn(self):
		del self._MssngValtn
		self._MssngValtn = None

	@property
	def AbnrmlVals(self):
		return self._AbnrmlVals

	@AbnrmlVals.setter
	def AbnrmlVals(self, value):
		self._AbnrmlVals = value if type(value) != auto else self.make_default("AbnrmlVals")

	@AbnrmlVals.deleter
	def AbnrmlVals(self):
		del self._AbnrmlVals
		self._AbnrmlVals = None

	@property
	def RefDt(self):
		return self._RefDt

	@RefDt.setter
	def RefDt(self, value):
		self._RefDt = value if type(value) != auto else self.make_default("RefDt")

	@RefDt.deleter
	def RefDt(self):
		del self._RefDt
		self._RefDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MssngMrgnInf', type=DetailedMissingMarginInformationStatistics4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MssngValtn', type=DetailedMissingValuationsStatistics4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AbnrmlVals', type=DetailedAbnormalValuesStatistics4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

