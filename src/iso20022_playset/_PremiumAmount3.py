# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ActiveOrHistoricCurrencyCode
from . import ISODate
from . import Max35Text
from . import Number
from . import PremiumQuote1Choice

class PremiumAmount3(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_DcmlPlcs", "_PrmCcy", "_PrmQt", "_PrmSttlmDt", "_PyerPtyRef", "_RcvrPtyRef"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def DcmlPlcs(self):
		return self._DcmlPlcs

	@DcmlPlcs.setter
	def DcmlPlcs(self, value):
		self._DcmlPlcs = value if value is not None else base_types.UninitialisedField(self, 'DcmlPlcs', Number, False)

	@DcmlPlcs.deleter
	def DcmlPlcs(self):
		del self._DcmlPlcs
		self._DcmlPlcs = base_types.UninitialisedField(self, 'DcmlPlcs', Number, False)

	@property
	def PrmCcy(self):
		return self._PrmCcy

	@PrmCcy.setter
	def PrmCcy(self, value):
		self._PrmCcy = value if value is not None else base_types.UninitialisedField(self, 'PrmCcy', ActiveOrHistoricCurrencyCode, False)

	@PrmCcy.deleter
	def PrmCcy(self):
		del self._PrmCcy
		self._PrmCcy = base_types.UninitialisedField(self, 'PrmCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def PrmQt(self):
		return self._PrmQt

	@PrmQt.setter
	def PrmQt(self, value):
		self._PrmQt = value if value is not None else base_types.UninitialisedField(self, 'PrmQt', PremiumQuote1Choice, False)

	@PrmQt.deleter
	def PrmQt(self):
		del self._PrmQt
		self._PrmQt = base_types.UninitialisedField(self, 'PrmQt', PremiumQuote1Choice, False)

	@property
	def PrmSttlmDt(self):
		return self._PrmSttlmDt

	@PrmSttlmDt.setter
	def PrmSttlmDt(self, value):
		self._PrmSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'PrmSttlmDt', ISODate, False)

	@PrmSttlmDt.deleter
	def PrmSttlmDt(self):
		del self._PrmSttlmDt
		self._PrmSttlmDt = base_types.UninitialisedField(self, 'PrmSttlmDt', ISODate, False)

	@property
	def PyerPtyRef(self):
		return self._PyerPtyRef

	@PyerPtyRef.setter
	def PyerPtyRef(self, value):
		self._PyerPtyRef = value if value is not None else base_types.UninitialisedField(self, 'PyerPtyRef', Max35Text, False)

	@PyerPtyRef.deleter
	def PyerPtyRef(self):
		del self._PyerPtyRef
		self._PyerPtyRef = base_types.UninitialisedField(self, 'PyerPtyRef', Max35Text, False)

	@property
	def RcvrPtyRef(self):
		return self._RcvrPtyRef

	@RcvrPtyRef.setter
	def RcvrPtyRef(self, value):
		self._RcvrPtyRef = value if value is not None else base_types.UninitialisedField(self, 'RcvrPtyRef', Max35Text, False)

	@RcvrPtyRef.deleter
	def RcvrPtyRef(self):
		del self._RcvrPtyRef
		self._RcvrPtyRef = base_types.UninitialisedField(self, 'RcvrPtyRef', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DcmlPlcs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmQt', type=PremiumQuote1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmSttlmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyerPtyRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrPtyRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))