# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BankContactPerson1Choice
from . import Baseline5
from . import ContactIdentification1
from . import ContactIdentification3
from . import MessageIdentification1
from . import SimpleIdentificationInformation

class BaselineReSubmissionV05(base_types._BaseFieldType):

	__slots__ = ["_Baseln", "_BkCtctPrsn", "_BuyrCtctPrsn", "_OthrBkCtctPrsn", "_SellrCtctPrsn", "_SubmissnId", "_SubmitrTxRef", "_TxId"]
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
	def BkCtctPrsn(self):
		return self._BkCtctPrsn

	@BkCtctPrsn.setter
	def BkCtctPrsn(self, value):
		self._BkCtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'BkCtctPrsn', BankContactPerson1Choice, False)

	@BkCtctPrsn.deleter
	def BkCtctPrsn(self):
		del self._BkCtctPrsn
		self._BkCtctPrsn = base_types.UninitialisedField(self, 'BkCtctPrsn', BankContactPerson1Choice, False)

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
	def SubmissnId(self):
		return self._SubmissnId

	@SubmissnId.setter
	def SubmissnId(self, value):
		self._SubmissnId = value if value is not None else base_types.UninitialisedField(self, 'SubmissnId', MessageIdentification1, False)

	@SubmissnId.deleter
	def SubmissnId(self):
		del self._SubmissnId
		self._SubmissnId = base_types.UninitialisedField(self, 'SubmissnId', MessageIdentification1, False)

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
		base_types.FieldEntry(name='BkCtctPrsn', type=BankContactPerson1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrBkCtctPrsn', type=ContactIdentification3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SellrCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmissnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
	))