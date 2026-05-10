import base_types
import Cleared16Choice
import PrincipalAmount3
import SecuritiesTransactionPrice19Choice
import ISODateTime
import MasterAgreement7
import Max52Text
import MICIdentifier
import ISODate
import SpecialCollateral1Code

class LoanData144(base_types._BaseFieldType):

	__slots__ = ["_MstrAgrmt", "_UnqTradIdr", "_UnitPric", "_EvtDt", "_TradgVn", "_ValDt", "_TermntnDt", "_MtrtyDt", "_ExctnDtTm", "_PrncplAmt", "_GnlColl", "_ClrSts"]
	@property
	def MstrAgrmt(self):
		return self._MstrAgrmt

	@MstrAgrmt.setter
	def MstrAgrmt(self, value):
		self._MstrAgrmt = value if type(value) != auto else self.make_default("MstrAgrmt")

	@MstrAgrmt.deleter
	def MstrAgrmt(self):
		del self._MstrAgrmt
		self._MstrAgrmt = None

	@property
	def UnqTradIdr(self):
		return self._UnqTradIdr

	@UnqTradIdr.setter
	def UnqTradIdr(self, value):
		self._UnqTradIdr = value if type(value) != auto else self.make_default("UnqTradIdr")

	@UnqTradIdr.deleter
	def UnqTradIdr(self):
		del self._UnqTradIdr
		self._UnqTradIdr = None

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	@property
	def EvtDt(self):
		return self._EvtDt

	@EvtDt.setter
	def EvtDt(self, value):
		self._EvtDt = value if type(value) != auto else self.make_default("EvtDt")

	@EvtDt.deleter
	def EvtDt(self):
		del self._EvtDt
		self._EvtDt = None

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if type(value) != auto else self.make_default("TradgVn")

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if type(value) != auto else self.make_default("TermntnDt")

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def ExctnDtTm(self):
		return self._ExctnDtTm

	@ExctnDtTm.setter
	def ExctnDtTm(self, value):
		self._ExctnDtTm = value if type(value) != auto else self.make_default("ExctnDtTm")

	@ExctnDtTm.deleter
	def ExctnDtTm(self):
		del self._ExctnDtTm
		self._ExctnDtTm = None

	@property
	def PrncplAmt(self):
		return self._PrncplAmt

	@PrncplAmt.setter
	def PrncplAmt(self, value):
		self._PrncplAmt = value if type(value) != auto else self.make_default("PrncplAmt")

	@PrncplAmt.deleter
	def PrncplAmt(self):
		del self._PrncplAmt
		self._PrncplAmt = None

	@property
	def GnlColl(self):
		return self._GnlColl

	@GnlColl.setter
	def GnlColl(self, value):
		self._GnlColl = value if type(value) != auto else self.make_default("GnlColl")

	@GnlColl.deleter
	def GnlColl(self):
		del self._GnlColl
		self._GnlColl = None

	@property
	def ClrSts(self):
		return self._ClrSts

	@ClrSts.setter
	def ClrSts(self, value):
		self._ClrSts = value if type(value) != auto else self.make_default("ClrSts")

	@ClrSts.deleter
	def ClrSts(self):
		del self._ClrSts
		self._ClrSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MstrAgrmt', type=MasterAgreement7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTradIdr', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=SecuritiesTransactionPrice19Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplAmt', type=PrincipalAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlColl', type=SpecialCollateral1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSts', type=Cleared16Choice, min=1, max=1, mutex_group=None, array=False),
	))

