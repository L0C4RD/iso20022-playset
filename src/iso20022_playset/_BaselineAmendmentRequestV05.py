# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Baseline5
from . import ContactIdentification1
from . import ContactIdentification3
from . import MessageIdentification1
from . import SimpleIdentificationInformation

class BaselineAmendmentRequestV05(base_types._BaseFieldType):

	__slots__ = ["_Baseln", "_BuyrBkCtctPrsn", "_BuyrCtctPrsn", "_OthrBkCtctPrsn", "_ReqId", "_SellrBkCtctPrsn", "_SellrCtctPrsn", "_SubmitrTxRef", "_TxId"]
	@property
	def Baseln(self):
		return self._Baseln

	@Baseln.setter
	def Baseln(self, value):
		self._Baseln = value if value is not None else base_types.UninitialisedField(self, 'Baseln', Baseline5, False)

	@Baseln.deleter
	def Baseln(self):
		del self._Baseln
		self._Baseln = base_types.UninitialisedField(self, 'Baseln', Baseline5, False)

	@property
	def BuyrBkCtctPrsn(self):
		return self._BuyrBkCtctPrsn

	@BuyrBkCtctPrsn.setter
	def BuyrBkCtctPrsn(self, value):
		self._BuyrBkCtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'BuyrBkCtctPrsn', ContactIdentification1, True)

	@BuyrBkCtctPrsn.deleter
	def BuyrBkCtctPrsn(self):
		del self._BuyrBkCtctPrsn
		self._BuyrBkCtctPrsn = base_types.UninitialisedField(self, 'BuyrBkCtctPrsn', ContactIdentification1, True)

	@property
	def BuyrCtctPrsn(self):
		return self._BuyrCtctPrsn

	@BuyrCtctPrsn.setter
	def BuyrCtctPrsn(self, value):
		self._BuyrCtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'BuyrCtctPrsn', ContactIdentification1, True)

	@BuyrCtctPrsn.deleter
	def BuyrCtctPrsn(self):
		del self._BuyrCtctPrsn
		self._BuyrCtctPrsn = base_types.UninitialisedField(self, 'BuyrCtctPrsn', ContactIdentification1, True)

	@property
	def OthrBkCtctPrsn(self):
		return self._OthrBkCtctPrsn

	@OthrBkCtctPrsn.setter
	def OthrBkCtctPrsn(self, value):
		self._OthrBkCtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'OthrBkCtctPrsn', ContactIdentification3, True)

	@OthrBkCtctPrsn.deleter
	def OthrBkCtctPrsn(self):
		del self._OthrBkCtctPrsn
		self._OthrBkCtctPrsn = base_types.UninitialisedField(self, 'OthrBkCtctPrsn', ContactIdentification3, True)

	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if value is not None else base_types.UninitialisedField(self, 'ReqId', MessageIdentification1, False)

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = base_types.UninitialisedField(self, 'ReqId', MessageIdentification1, False)

	@property
	def SellrBkCtctPrsn(self):
		return self._SellrBkCtctPrsn

	@SellrBkCtctPrsn.setter
	def SellrBkCtctPrsn(self, value):
		self._SellrBkCtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'SellrBkCtctPrsn', ContactIdentification1, True)

	@SellrBkCtctPrsn.deleter
	def SellrBkCtctPrsn(self):
		del self._SellrBkCtctPrsn
		self._SellrBkCtctPrsn = base_types.UninitialisedField(self, 'SellrBkCtctPrsn', ContactIdentification1, True)

	@property
	def SellrCtctPrsn(self):
		return self._SellrCtctPrsn

	@SellrCtctPrsn.setter
	def SellrCtctPrsn(self, value):
		self._SellrCtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'SellrCtctPrsn', ContactIdentification1, True)

	@SellrCtctPrsn.deleter
	def SellrCtctPrsn(self):
		del self._SellrCtctPrsn
		self._SellrCtctPrsn = base_types.UninitialisedField(self, 'SellrCtctPrsn', ContactIdentification1, True)

	@property
	def SubmitrTxRef(self):
		return self._SubmitrTxRef

	@SubmitrTxRef.setter
	def SubmitrTxRef(self, value):
		self._SubmitrTxRef = value if value is not None else base_types.UninitialisedField(self, 'SubmitrTxRef', SimpleIdentificationInformation, False)

	@SubmitrTxRef.deleter
	def SubmitrTxRef(self):
		del self._SubmitrTxRef
		self._SubmitrTxRef = base_types.UninitialisedField(self, 'SubmitrTxRef', SimpleIdentificationInformation, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', SimpleIdentificationInformation, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', SimpleIdentificationInformation, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Baseln', type=Baseline5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrBkCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrBkCtctPrsn', type=ContactIdentification3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBkCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SellrCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
	))