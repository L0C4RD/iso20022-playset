# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CopyDuplicate1Code
from . import DateAndDateTime2Choice
from . import Max35Text
from . import PartyIdentification136

class TransactionAndDocumentIdentification6(base_types._BaseFieldType):

	__slots__ = ["_CpyDplct", "_CreDtTm", "_DocId", "_MsgOrgtr", "_MsgRcpt", "_TxId"]
	@property
	def CpyDplct(self):
		return self._CpyDplct

	@CpyDplct.setter
	def CpyDplct(self, value):
		self._CpyDplct = value if value is not None else base_types.UninitialisedField(self, 'CpyDplct', CopyDuplicate1Code, False)

	@CpyDplct.deleter
	def CpyDplct(self):
		del self._CpyDplct
		self._CpyDplct = base_types.UninitialisedField(self, 'CpyDplct', CopyDuplicate1Code, False)

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', DateAndDateTime2Choice, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', DateAndDateTime2Choice, False)

	@property
	def DocId(self):
		return self._DocId

	@DocId.setter
	def DocId(self, value):
		self._DocId = value if value is not None else base_types.UninitialisedField(self, 'DocId', Max35Text, False)

	@DocId.deleter
	def DocId(self):
		del self._DocId
		self._DocId = base_types.UninitialisedField(self, 'DocId', Max35Text, False)

	@property
	def MsgOrgtr(self):
		return self._MsgOrgtr

	@MsgOrgtr.setter
	def MsgOrgtr(self, value):
		self._MsgOrgtr = value if value is not None else base_types.UninitialisedField(self, 'MsgOrgtr', PartyIdentification136, False)

	@MsgOrgtr.deleter
	def MsgOrgtr(self):
		del self._MsgOrgtr
		self._MsgOrgtr = base_types.UninitialisedField(self, 'MsgOrgtr', PartyIdentification136, False)

	@property
	def MsgRcpt(self):
		return self._MsgRcpt

	@MsgRcpt.setter
	def MsgRcpt(self, value):
		self._MsgRcpt = value if value is not None else base_types.UninitialisedField(self, 'MsgRcpt', PartyIdentification136, False)

	@MsgRcpt.deleter
	def MsgRcpt(self):
		del self._MsgRcpt
		self._MsgRcpt = base_types.UninitialisedField(self, 'MsgRcpt', PartyIdentification136, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CpyDplct', type=CopyDuplicate1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgOrgtr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRcpt', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))