# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountOrPercentage2Choice
from . import BICIdentification1
from . import BPOApplicableRules1Choice
from . import Charges5
from . import CountryCode
from . import ISODate
from . import Location2
from . import PaymentTerms4
from . import SettlementTerms3

class PaymentObligation2(base_types._BaseFieldType):

	__slots__ = ["_AplblLaw", "_AplblRules", "_Chrgs", "_OblgrBk", "_PlcOfJursdctn", "_PmtOblgtnAmt", "_PmtTerms", "_RcptBk", "_SttlmTerms", "_XpryDt"]
	@property
	def AplblLaw(self):
		return self._AplblLaw

	@AplblLaw.setter
	def AplblLaw(self, value):
		self._AplblLaw = value if value is not None else base_types.UninitialisedField(self, 'AplblLaw', CountryCode, False)

	@AplblLaw.deleter
	def AplblLaw(self):
		del self._AplblLaw
		self._AplblLaw = base_types.UninitialisedField(self, 'AplblLaw', CountryCode, False)

	@property
	def AplblRules(self):
		return self._AplblRules

	@AplblRules.setter
	def AplblRules(self, value):
		self._AplblRules = value if value is not None else base_types.UninitialisedField(self, 'AplblRules', BPOApplicableRules1Choice, False)

	@AplblRules.deleter
	def AplblRules(self):
		del self._AplblRules
		self._AplblRules = base_types.UninitialisedField(self, 'AplblRules', BPOApplicableRules1Choice, False)

	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if value is not None else base_types.UninitialisedField(self, 'Chrgs', Charges5, True)

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = base_types.UninitialisedField(self, 'Chrgs', Charges5, True)

	@property
	def OblgrBk(self):
		return self._OblgrBk

	@OblgrBk.setter
	def OblgrBk(self, value):
		self._OblgrBk = value if value is not None else base_types.UninitialisedField(self, 'OblgrBk', BICIdentification1, False)

	@OblgrBk.deleter
	def OblgrBk(self):
		del self._OblgrBk
		self._OblgrBk = base_types.UninitialisedField(self, 'OblgrBk', BICIdentification1, False)

	@property
	def PlcOfJursdctn(self):
		return self._PlcOfJursdctn

	@PlcOfJursdctn.setter
	def PlcOfJursdctn(self, value):
		self._PlcOfJursdctn = value if value is not None else base_types.UninitialisedField(self, 'PlcOfJursdctn', Location2, False)

	@PlcOfJursdctn.deleter
	def PlcOfJursdctn(self):
		del self._PlcOfJursdctn
		self._PlcOfJursdctn = base_types.UninitialisedField(self, 'PlcOfJursdctn', Location2, False)

	@property
	def PmtOblgtnAmt(self):
		return self._PmtOblgtnAmt

	@PmtOblgtnAmt.setter
	def PmtOblgtnAmt(self, value):
		self._PmtOblgtnAmt = value if value is not None else base_types.UninitialisedField(self, 'PmtOblgtnAmt', AmountOrPercentage2Choice, False)

	@PmtOblgtnAmt.deleter
	def PmtOblgtnAmt(self):
		del self._PmtOblgtnAmt
		self._PmtOblgtnAmt = base_types.UninitialisedField(self, 'PmtOblgtnAmt', AmountOrPercentage2Choice, False)

	@property
	def PmtTerms(self):
		return self._PmtTerms

	@PmtTerms.setter
	def PmtTerms(self, value):
		self._PmtTerms = value if value is not None else base_types.UninitialisedField(self, 'PmtTerms', PaymentTerms4, True)

	@PmtTerms.deleter
	def PmtTerms(self):
		del self._PmtTerms
		self._PmtTerms = base_types.UninitialisedField(self, 'PmtTerms', PaymentTerms4, True)

	@property
	def RcptBk(self):
		return self._RcptBk

	@RcptBk.setter
	def RcptBk(self, value):
		self._RcptBk = value if value is not None else base_types.UninitialisedField(self, 'RcptBk', BICIdentification1, False)

	@RcptBk.deleter
	def RcptBk(self):
		del self._RcptBk
		self._RcptBk = base_types.UninitialisedField(self, 'RcptBk', BICIdentification1, False)

	@property
	def SttlmTerms(self):
		return self._SttlmTerms

	@SttlmTerms.setter
	def SttlmTerms(self, value):
		self._SttlmTerms = value if value is not None else base_types.UninitialisedField(self, 'SttlmTerms', SettlementTerms3, False)

	@SttlmTerms.deleter
	def SttlmTerms(self):
		del self._SttlmTerms
		self._SttlmTerms = base_types.UninitialisedField(self, 'SttlmTerms', SettlementTerms3, False)

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if value is not None else base_types.UninitialisedField(self, 'XpryDt', ISODate, False)

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = base_types.UninitialisedField(self, 'XpryDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AplblLaw', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AplblRules', type=BPOApplicableRules1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrgs', type=Charges5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OblgrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfJursdctn', type=Location2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtOblgtnAmt', type=AmountOrPercentage2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTerms', type=PaymentTerms4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcptBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTerms', type=SettlementTerms3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))