# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICIdentification1
from . import CountryCode
from . import Max35Text
from . import PartyIdentification28
from . import PendingActivity1
from . import TransactionStatus4

class ReportSpecification4(base_types._BaseFieldType):

	__slots__ = ["_Buyr", "_BuyrCtry", "_Crspdt", "_CrspdtCtry", "_NttiesToBeRptd", "_OblgrBk", "_PdgReqForActn", "_Sellr", "_SellrCtry", "_SubmitgBk", "_SubmitrTxRef", "_TxId", "_TxSts"]
	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if value is not None else base_types.UninitialisedField(self, 'Buyr', PartyIdentification28, True)

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = base_types.UninitialisedField(self, 'Buyr', PartyIdentification28, True)

	@property
	def BuyrCtry(self):
		return self._BuyrCtry

	@BuyrCtry.setter
	def BuyrCtry(self, value):
		self._BuyrCtry = value if value is not None else base_types.UninitialisedField(self, 'BuyrCtry', CountryCode, True)

	@BuyrCtry.deleter
	def BuyrCtry(self):
		del self._BuyrCtry
		self._BuyrCtry = base_types.UninitialisedField(self, 'BuyrCtry', CountryCode, True)

	@property
	def Crspdt(self):
		return self._Crspdt

	@Crspdt.setter
	def Crspdt(self, value):
		self._Crspdt = value if value is not None else base_types.UninitialisedField(self, 'Crspdt', BICIdentification1, True)

	@Crspdt.deleter
	def Crspdt(self):
		del self._Crspdt
		self._Crspdt = base_types.UninitialisedField(self, 'Crspdt', BICIdentification1, True)

	@property
	def CrspdtCtry(self):
		return self._CrspdtCtry

	@CrspdtCtry.setter
	def CrspdtCtry(self, value):
		self._CrspdtCtry = value if value is not None else base_types.UninitialisedField(self, 'CrspdtCtry', CountryCode, True)

	@CrspdtCtry.deleter
	def CrspdtCtry(self):
		del self._CrspdtCtry
		self._CrspdtCtry = base_types.UninitialisedField(self, 'CrspdtCtry', CountryCode, True)

	@property
	def NttiesToBeRptd(self):
		return self._NttiesToBeRptd

	@NttiesToBeRptd.setter
	def NttiesToBeRptd(self, value):
		self._NttiesToBeRptd = value if value is not None else base_types.UninitialisedField(self, 'NttiesToBeRptd', BICIdentification1, True)

	@NttiesToBeRptd.deleter
	def NttiesToBeRptd(self):
		del self._NttiesToBeRptd
		self._NttiesToBeRptd = base_types.UninitialisedField(self, 'NttiesToBeRptd', BICIdentification1, True)

	@property
	def OblgrBk(self):
		return self._OblgrBk

	@OblgrBk.setter
	def OblgrBk(self, value):
		self._OblgrBk = value if value is not None else base_types.UninitialisedField(self, 'OblgrBk', BICIdentification1, True)

	@OblgrBk.deleter
	def OblgrBk(self):
		del self._OblgrBk
		self._OblgrBk = base_types.UninitialisedField(self, 'OblgrBk', BICIdentification1, True)

	@property
	def PdgReqForActn(self):
		return self._PdgReqForActn

	@PdgReqForActn.setter
	def PdgReqForActn(self, value):
		self._PdgReqForActn = value if value is not None else base_types.UninitialisedField(self, 'PdgReqForActn', PendingActivity1, True)

	@PdgReqForActn.deleter
	def PdgReqForActn(self):
		del self._PdgReqForActn
		self._PdgReqForActn = base_types.UninitialisedField(self, 'PdgReqForActn', PendingActivity1, True)

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if value is not None else base_types.UninitialisedField(self, 'Sellr', PartyIdentification28, True)

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = base_types.UninitialisedField(self, 'Sellr', PartyIdentification28, True)

	@property
	def SellrCtry(self):
		return self._SellrCtry

	@SellrCtry.setter
	def SellrCtry(self, value):
		self._SellrCtry = value if value is not None else base_types.UninitialisedField(self, 'SellrCtry', CountryCode, True)

	@SellrCtry.deleter
	def SellrCtry(self):
		del self._SellrCtry
		self._SellrCtry = base_types.UninitialisedField(self, 'SellrCtry', CountryCode, True)

	@property
	def SubmitgBk(self):
		return self._SubmitgBk

	@SubmitgBk.setter
	def SubmitgBk(self, value):
		self._SubmitgBk = value if value is not None else base_types.UninitialisedField(self, 'SubmitgBk', BICIdentification1, True)

	@SubmitgBk.deleter
	def SubmitgBk(self):
		del self._SubmitgBk
		self._SubmitgBk = base_types.UninitialisedField(self, 'SubmitgBk', BICIdentification1, True)

	@property
	def SubmitrTxRef(self):
		return self._SubmitrTxRef

	@SubmitrTxRef.setter
	def SubmitrTxRef(self, value):
		self._SubmitrTxRef = value if value is not None else base_types.UninitialisedField(self, 'SubmitrTxRef', Max35Text, True)

	@SubmitrTxRef.deleter
	def SubmitrTxRef(self):
		del self._SubmitrTxRef
		self._SubmitrTxRef = base_types.UninitialisedField(self, 'SubmitrTxRef', Max35Text, True)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, True)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, True)

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if value is not None else base_types.UninitialisedField(self, 'TxSts', TransactionStatus4, True)

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = base_types.UninitialisedField(self, 'TxSts', TransactionStatus4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Buyr', type=PartyIdentification28, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Crspdt', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CrspdtCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NttiesToBeRptd', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OblgrBk', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdgReqForActn', type=PendingActivity1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification28, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SellrCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitgBk', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitrTxRef', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=0, max=None, mutex_group=None, array=True),
	))