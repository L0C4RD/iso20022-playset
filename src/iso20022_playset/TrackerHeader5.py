import base_types
import ServiceLevel8Choice
import Max35Text
import Max15NumericText
import ISODateTime
import OriginalBusinessInstruction1
import TrackerPartyIdentification2

class TrackerHeader5(base_types._BaseFieldType):

	__slots__ = ["_SvcLvl", "_MsgId", "_TrckrInfrmdPty", "_TrckrInfrmgPty", "_CreDtTm", "_NbOfTxs", "_OrgnlTrckrUpd"]
	@property
	def SvcLvl(self):
		return self._SvcLvl

	@SvcLvl.setter
	def SvcLvl(self, value):
		self._SvcLvl = value if type(value) != auto else self.make_default("SvcLvl")

	@SvcLvl.deleter
	def SvcLvl(self):
		del self._SvcLvl
		self._SvcLvl = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def TrckrInfrmdPty(self):
		return self._TrckrInfrmdPty

	@TrckrInfrmdPty.setter
	def TrckrInfrmdPty(self, value):
		self._TrckrInfrmdPty = value if type(value) != auto else self.make_default("TrckrInfrmdPty")

	@TrckrInfrmdPty.deleter
	def TrckrInfrmdPty(self):
		del self._TrckrInfrmdPty
		self._TrckrInfrmdPty = None

	@property
	def TrckrInfrmgPty(self):
		return self._TrckrInfrmgPty

	@TrckrInfrmgPty.setter
	def TrckrInfrmgPty(self, value):
		self._TrckrInfrmgPty = value if type(value) != auto else self.make_default("TrckrInfrmgPty")

	@TrckrInfrmgPty.deleter
	def TrckrInfrmgPty(self):
		del self._TrckrInfrmgPty
		self._TrckrInfrmgPty = None

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

	@property
	def NbOfTxs(self):
		return self._NbOfTxs

	@NbOfTxs.setter
	def NbOfTxs(self, value):
		self._NbOfTxs = value if type(value) != auto else self.make_default("NbOfTxs")

	@NbOfTxs.deleter
	def NbOfTxs(self):
		del self._NbOfTxs
		self._NbOfTxs = None

	@property
	def OrgnlTrckrUpd(self):
		return self._OrgnlTrckrUpd

	@OrgnlTrckrUpd.setter
	def OrgnlTrckrUpd(self, value):
		self._OrgnlTrckrUpd = value if type(value) != auto else self.make_default("OrgnlTrckrUpd")

	@OrgnlTrckrUpd.deleter
	def OrgnlTrckrUpd(self):
		del self._OrgnlTrckrUpd
		self._OrgnlTrckrUpd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcLvl', type=ServiceLevel8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckrInfrmdPty', type=TrackerPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckrInfrmgPty', type=TrackerPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTrckrUpd', type=OriginalBusinessInstruction1, min=0, max=1, mutex_group=None, array=False),
	))

