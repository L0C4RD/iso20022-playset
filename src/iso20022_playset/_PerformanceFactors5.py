# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DatePeriod2
from . import DecimalNumber

class PerformanceFactors5(base_types._BaseFieldType):

	__slots__ = ["_AcmltnPrd", "_CmltvCorpActnFctr", "_CorpActnFctr", "_NrmlPrfrmnc"]
	@property
	def AcmltnPrd(self):
		return self._AcmltnPrd

	@AcmltnPrd.setter
	def AcmltnPrd(self, value):
		self._AcmltnPrd = value if value is not None else base_types.UninitialisedField(self, 'AcmltnPrd', DatePeriod2, False)

	@AcmltnPrd.deleter
	def AcmltnPrd(self):
		del self._AcmltnPrd
		self._AcmltnPrd = base_types.UninitialisedField(self, 'AcmltnPrd', DatePeriod2, False)

	@property
	def CmltvCorpActnFctr(self):
		return self._CmltvCorpActnFctr

	@CmltvCorpActnFctr.setter
	def CmltvCorpActnFctr(self, value):
		self._CmltvCorpActnFctr = value if value is not None else base_types.UninitialisedField(self, 'CmltvCorpActnFctr', DecimalNumber, False)

	@CmltvCorpActnFctr.deleter
	def CmltvCorpActnFctr(self):
		del self._CmltvCorpActnFctr
		self._CmltvCorpActnFctr = base_types.UninitialisedField(self, 'CmltvCorpActnFctr', DecimalNumber, False)

	@property
	def CorpActnFctr(self):
		return self._CorpActnFctr

	@CorpActnFctr.setter
	def CorpActnFctr(self, value):
		self._CorpActnFctr = value if value is not None else base_types.UninitialisedField(self, 'CorpActnFctr', DecimalNumber, False)

	@CorpActnFctr.deleter
	def CorpActnFctr(self):
		del self._CorpActnFctr
		self._CorpActnFctr = base_types.UninitialisedField(self, 'CorpActnFctr', DecimalNumber, False)

	@property
	def NrmlPrfrmnc(self):
		return self._NrmlPrfrmnc

	@NrmlPrfrmnc.setter
	def NrmlPrfrmnc(self, value):
		self._NrmlPrfrmnc = value if value is not None else base_types.UninitialisedField(self, 'NrmlPrfrmnc', DecimalNumber, False)

	@NrmlPrfrmnc.deleter
	def NrmlPrfrmnc(self):
		del self._NrmlPrfrmnc
		self._NrmlPrfrmnc = base_types.UninitialisedField(self, 'NrmlPrfrmnc', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcmltnPrd', type=DatePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmltvCorpActnFctr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnFctr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrmlPrfrmnc', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))