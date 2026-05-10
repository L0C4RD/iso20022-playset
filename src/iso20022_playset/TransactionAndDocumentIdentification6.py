from . import base_types
import CopyDuplicate1Code
import PartyIdentification136
import DateAndDateTime2Choice
import Max35Text

class TransactionAndDocumentIdentification6(base_types._BaseFieldType):

	__slots__ = ["_MsgOrgtr", "_TxId", "_CpyDplct", "_MsgRcpt", "_DocId", "_CreDtTm"]
	@property
	def MsgOrgtr(self):
		return self._MsgOrgtr

	@MsgOrgtr.setter
	def MsgOrgtr(self, value):
		self._MsgOrgtr = value if type(value) != auto else self.make_default("MsgOrgtr")

	@MsgOrgtr.deleter
	def MsgOrgtr(self):
		del self._MsgOrgtr
		self._MsgOrgtr = None

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
	def CpyDplct(self):
		return self._CpyDplct

	@CpyDplct.setter
	def CpyDplct(self, value):
		self._CpyDplct = value if type(value) != auto else self.make_default("CpyDplct")

	@CpyDplct.deleter
	def CpyDplct(self):
		del self._CpyDplct
		self._CpyDplct = None

	@property
	def MsgRcpt(self):
		return self._MsgRcpt

	@MsgRcpt.setter
	def MsgRcpt(self, value):
		self._MsgRcpt = value if type(value) != auto else self.make_default("MsgRcpt")

	@MsgRcpt.deleter
	def MsgRcpt(self):
		del self._MsgRcpt
		self._MsgRcpt = None

	@property
	def DocId(self):
		return self._DocId

	@DocId.setter
	def DocId(self, value):
		self._DocId = value if type(value) != auto else self.make_default("DocId")

	@DocId.deleter
	def DocId(self):
		del self._DocId
		self._DocId = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgOrgtr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpyDplct', type=CopyDuplicate1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRcpt', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

