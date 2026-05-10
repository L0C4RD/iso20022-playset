import base_types
import Max35Text
import PremiumQuote1Choice
import Number
import ActiveCurrencyAndAmount
import ISODate
import ActiveOrHistoricCurrencyCode

class PremiumAmount3(base_types._BaseFieldType):

	__slots__ = ["_PrmSttlmDt", "_RcvrPtyRef", "_DcmlPlcs", "_PyerPtyRef", "_PrmCcy", "_PrmQt", "_Amt"]
	@property
	def PrmSttlmDt(self):
		return self._PrmSttlmDt

	@PrmSttlmDt.setter
	def PrmSttlmDt(self, value):
		self._PrmSttlmDt = value if type(value) != auto else self.make_default("PrmSttlmDt")

	@PrmSttlmDt.deleter
	def PrmSttlmDt(self):
		del self._PrmSttlmDt
		self._PrmSttlmDt = None

	@property
	def RcvrPtyRef(self):
		return self._RcvrPtyRef

	@RcvrPtyRef.setter
	def RcvrPtyRef(self, value):
		self._RcvrPtyRef = value if type(value) != auto else self.make_default("RcvrPtyRef")

	@RcvrPtyRef.deleter
	def RcvrPtyRef(self):
		del self._RcvrPtyRef
		self._RcvrPtyRef = None

	@property
	def DcmlPlcs(self):
		return self._DcmlPlcs

	@DcmlPlcs.setter
	def DcmlPlcs(self, value):
		self._DcmlPlcs = value if type(value) != auto else self.make_default("DcmlPlcs")

	@DcmlPlcs.deleter
	def DcmlPlcs(self):
		del self._DcmlPlcs
		self._DcmlPlcs = None

	@property
	def PyerPtyRef(self):
		return self._PyerPtyRef

	@PyerPtyRef.setter
	def PyerPtyRef(self, value):
		self._PyerPtyRef = value if type(value) != auto else self.make_default("PyerPtyRef")

	@PyerPtyRef.deleter
	def PyerPtyRef(self):
		del self._PyerPtyRef
		self._PyerPtyRef = None

	@property
	def PrmCcy(self):
		return self._PrmCcy

	@PrmCcy.setter
	def PrmCcy(self, value):
		self._PrmCcy = value if type(value) != auto else self.make_default("PrmCcy")

	@PrmCcy.deleter
	def PrmCcy(self):
		del self._PrmCcy
		self._PrmCcy = None

	@property
	def PrmQt(self):
		return self._PrmQt

	@PrmQt.setter
	def PrmQt(self, value):
		self._PrmQt = value if type(value) != auto else self.make_default("PrmQt")

	@PrmQt.deleter
	def PrmQt(self):
		del self._PrmQt
		self._PrmQt = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrmSttlmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrPtyRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DcmlPlcs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyerPtyRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmQt', type=PremiumQuote1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

