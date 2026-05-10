from . import base_types
import DecimalNumber
import DatePeriodDetails

class PerformanceFactors1(base_types._BaseFieldType):

	__slots__ = ["_CmltvCorpActnFctr", "_AcmltnPrd", "_NrmlPrfrmnc", "_CorpActnFctr"]
	@property
	def CmltvCorpActnFctr(self):
		return self._CmltvCorpActnFctr

	@CmltvCorpActnFctr.setter
	def CmltvCorpActnFctr(self, value):
		self._CmltvCorpActnFctr = value if type(value) != auto else self.make_default("CmltvCorpActnFctr")

	@CmltvCorpActnFctr.deleter
	def CmltvCorpActnFctr(self):
		del self._CmltvCorpActnFctr
		self._CmltvCorpActnFctr = None

	@property
	def AcmltnPrd(self):
		return self._AcmltnPrd

	@AcmltnPrd.setter
	def AcmltnPrd(self, value):
		self._AcmltnPrd = value if type(value) != auto else self.make_default("AcmltnPrd")

	@AcmltnPrd.deleter
	def AcmltnPrd(self):
		del self._AcmltnPrd
		self._AcmltnPrd = None

	@property
	def NrmlPrfrmnc(self):
		return self._NrmlPrfrmnc

	@NrmlPrfrmnc.setter
	def NrmlPrfrmnc(self, value):
		self._NrmlPrfrmnc = value if type(value) != auto else self.make_default("NrmlPrfrmnc")

	@NrmlPrfrmnc.deleter
	def NrmlPrfrmnc(self):
		del self._NrmlPrfrmnc
		self._NrmlPrfrmnc = None

	@property
	def CorpActnFctr(self):
		return self._CorpActnFctr

	@CorpActnFctr.setter
	def CorpActnFctr(self, value):
		self._CorpActnFctr = value if type(value) != auto else self.make_default("CorpActnFctr")

	@CorpActnFctr.deleter
	def CorpActnFctr(self):
		del self._CorpActnFctr
		self._CorpActnFctr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmltvCorpActnFctr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcmltnPrd', type=DatePeriodDetails, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrmlPrfrmnc', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnFctr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

