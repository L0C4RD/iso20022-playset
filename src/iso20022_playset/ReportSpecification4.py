import base_types
import Max35Text
import BICIdentification1
import TransactionStatus4
import CountryCode
import PartyIdentification28
import PendingActivity1

class ReportSpecification4(base_types._BaseFieldType):

	__slots__ = ["_CrspdtCtry", "_TxSts", "_NttiesToBeRptd", "_SubmitgBk", "_OblgrBk", "_Sellr", "_PdgReqForActn", "_Buyr", "_SellrCtry", "_TxId", "_BuyrCtry", "_Crspdt", "_SubmitrTxRef"]
	@property
	def CrspdtCtry(self):
		return self._CrspdtCtry

	@CrspdtCtry.setter
	def CrspdtCtry(self, value):
		self._CrspdtCtry = value if type(value) != auto else self.make_default("CrspdtCtry")

	@CrspdtCtry.deleter
	def CrspdtCtry(self):
		del self._CrspdtCtry
		self._CrspdtCtry = None

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if type(value) != auto else self.make_default("TxSts")

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = None

	@property
	def NttiesToBeRptd(self):
		return self._NttiesToBeRptd

	@NttiesToBeRptd.setter
	def NttiesToBeRptd(self, value):
		self._NttiesToBeRptd = value if type(value) != auto else self.make_default("NttiesToBeRptd")

	@NttiesToBeRptd.deleter
	def NttiesToBeRptd(self):
		del self._NttiesToBeRptd
		self._NttiesToBeRptd = None

	@property
	def SubmitgBk(self):
		return self._SubmitgBk

	@SubmitgBk.setter
	def SubmitgBk(self, value):
		self._SubmitgBk = value if type(value) != auto else self.make_default("SubmitgBk")

	@SubmitgBk.deleter
	def SubmitgBk(self):
		del self._SubmitgBk
		self._SubmitgBk = None

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
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if type(value) != auto else self.make_default("Sellr")

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = None

	@property
	def PdgReqForActn(self):
		return self._PdgReqForActn

	@PdgReqForActn.setter
	def PdgReqForActn(self, value):
		self._PdgReqForActn = value if type(value) != auto else self.make_default("PdgReqForActn")

	@PdgReqForActn.deleter
	def PdgReqForActn(self):
		del self._PdgReqForActn
		self._PdgReqForActn = None

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	@property
	def SellrCtry(self):
		return self._SellrCtry

	@SellrCtry.setter
	def SellrCtry(self, value):
		self._SellrCtry = value if type(value) != auto else self.make_default("SellrCtry")

	@SellrCtry.deleter
	def SellrCtry(self):
		del self._SellrCtry
		self._SellrCtry = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def BuyrCtry(self):
		return self._BuyrCtry

	@BuyrCtry.setter
	def BuyrCtry(self, value):
		self._BuyrCtry = value if type(value) != auto else self.make_default("BuyrCtry")

	@BuyrCtry.deleter
	def BuyrCtry(self):
		del self._BuyrCtry
		self._BuyrCtry = None

	@property
	def Crspdt(self):
		return self._Crspdt

	@Crspdt.setter
	def Crspdt(self, value):
		self._Crspdt = value if type(value) != auto else self.make_default("Crspdt")

	@Crspdt.deleter
	def Crspdt(self):
		del self._Crspdt
		self._Crspdt = None

	@property
	def SubmitrTxRef(self):
		return self._SubmitrTxRef

	@SubmitrTxRef.setter
	def SubmitrTxRef(self, value):
		self._SubmitrTxRef = value if type(value) != auto else self.make_default("SubmitrTxRef")

	@SubmitrTxRef.deleter
	def SubmitrTxRef(self):
		del self._SubmitrTxRef
		self._SubmitrTxRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrspdtCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NttiesToBeRptd', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitgBk', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OblgrBk', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification28, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdgReqForActn', type=PendingActivity1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Buyr', type=PartyIdentification28, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SellrCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Crspdt', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitrTxRef', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
	))

