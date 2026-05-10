import base_types
import ISODate
import BICIdentification1
import PaymentTerms4
import SettlementTerms3
import AmountOrPercentage2Choice
import BPOApplicableRules1Choice
import Charges5
import CountryCode
import Location2

class PaymentObligation2(base_types._BaseFieldType):

	__slots__ = ["_AplblRules", "_AplblLaw", "_Chrgs", "_OblgrBk", "_PmtOblgtnAmt", "_XpryDt", "_PlcOfJursdctn", "_SttlmTerms", "_PmtTerms", "_RcptBk"]
	@property
	def AplblRules(self):
		return self._AplblRules

	@AplblRules.setter
	def AplblRules(self, value):
		self._AplblRules = value if type(value) != auto else self.make_default("AplblRules")

	@AplblRules.deleter
	def AplblRules(self):
		del self._AplblRules
		self._AplblRules = None

	@property
	def AplblLaw(self):
		return self._AplblLaw

	@AplblLaw.setter
	def AplblLaw(self, value):
		self._AplblLaw = value if type(value) != auto else self.make_default("AplblLaw")

	@AplblLaw.deleter
	def AplblLaw(self):
		del self._AplblLaw
		self._AplblLaw = None

	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if type(value) != auto else self.make_default("Chrgs")

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = None

	@property
	def OblgrBk(self):
		return self._OblgrBk

	@OblgrBk.setter
	def OblgrBk(self, value):
		self._OblgrBk = value if type(value) != auto else self.make_default("OblgrBk")

	@OblgrBk.deleter
	def OblgrBk(self):
		del self._OblgrBk
		self._OblgrBk = None

	@property
	def PmtOblgtnAmt(self):
		return self._PmtOblgtnAmt

	@PmtOblgtnAmt.setter
	def PmtOblgtnAmt(self, value):
		self._PmtOblgtnAmt = value if type(value) != auto else self.make_default("PmtOblgtnAmt")

	@PmtOblgtnAmt.deleter
	def PmtOblgtnAmt(self):
		del self._PmtOblgtnAmt
		self._PmtOblgtnAmt = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	@property
	def PlcOfJursdctn(self):
		return self._PlcOfJursdctn

	@PlcOfJursdctn.setter
	def PlcOfJursdctn(self, value):
		self._PlcOfJursdctn = value if type(value) != auto else self.make_default("PlcOfJursdctn")

	@PlcOfJursdctn.deleter
	def PlcOfJursdctn(self):
		del self._PlcOfJursdctn
		self._PlcOfJursdctn = None

	@property
	def SttlmTerms(self):
		return self._SttlmTerms

	@SttlmTerms.setter
	def SttlmTerms(self, value):
		self._SttlmTerms = value if type(value) != auto else self.make_default("SttlmTerms")

	@SttlmTerms.deleter
	def SttlmTerms(self):
		del self._SttlmTerms
		self._SttlmTerms = None

	@property
	def PmtTerms(self):
		return self._PmtTerms

	@PmtTerms.setter
	def PmtTerms(self, value):
		self._PmtTerms = value if type(value) != auto else self.make_default("PmtTerms")

	@PmtTerms.deleter
	def PmtTerms(self):
		del self._PmtTerms
		self._PmtTerms = None

	@property
	def RcptBk(self):
		return self._RcptBk

	@RcptBk.setter
	def RcptBk(self, value):
		self._RcptBk = value if type(value) != auto else self.make_default("RcptBk")

	@RcptBk.deleter
	def RcptBk(self):
		del self._RcptBk
		self._RcptBk = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AplblRules', type=BPOApplicableRules1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AplblLaw', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrgs', type=Charges5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OblgrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtOblgtnAmt', type=AmountOrPercentage2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfJursdctn', type=Location2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTerms', type=SettlementTerms3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTerms', type=PaymentTerms4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcptBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

