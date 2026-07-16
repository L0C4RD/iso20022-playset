# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max15NumericText
from . import Max35Text
from . import OriginalBusinessInstruction1
from . import ServiceLevel8Choice
from . import TrackerPartyIdentification2

class TrackerHeader5(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_MsgId", "_NbOfTxs", "_OrgnlTrckrUpd", "_SvcLvl", "_TrckrInfrmdPty", "_TrckrInfrmgPty"]
	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@property
	def NbOfTxs(self):
		return self._NbOfTxs

	@NbOfTxs.setter
	def NbOfTxs(self, value):
		self._NbOfTxs = value if value is not None else base_types.UninitialisedField(self, 'NbOfTxs', Max15NumericText, False)

	@NbOfTxs.deleter
	def NbOfTxs(self):
		del self._NbOfTxs
		self._NbOfTxs = base_types.UninitialisedField(self, 'NbOfTxs', Max15NumericText, False)

	@property
	def OrgnlTrckrUpd(self):
		return self._OrgnlTrckrUpd

	@OrgnlTrckrUpd.setter
	def OrgnlTrckrUpd(self, value):
		self._OrgnlTrckrUpd = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTrckrUpd', OriginalBusinessInstruction1, False)

	@OrgnlTrckrUpd.deleter
	def OrgnlTrckrUpd(self):
		del self._OrgnlTrckrUpd
		self._OrgnlTrckrUpd = base_types.UninitialisedField(self, 'OrgnlTrckrUpd', OriginalBusinessInstruction1, False)

	@property
	def SvcLvl(self):
		return self._SvcLvl

	@SvcLvl.setter
	def SvcLvl(self, value):
		self._SvcLvl = value if value is not None else base_types.UninitialisedField(self, 'SvcLvl', ServiceLevel8Choice, False)

	@SvcLvl.deleter
	def SvcLvl(self):
		del self._SvcLvl
		self._SvcLvl = base_types.UninitialisedField(self, 'SvcLvl', ServiceLevel8Choice, False)

	@property
	def TrckrInfrmdPty(self):
		return self._TrckrInfrmdPty

	@TrckrInfrmdPty.setter
	def TrckrInfrmdPty(self, value):
		self._TrckrInfrmdPty = value if value is not None else base_types.UninitialisedField(self, 'TrckrInfrmdPty', TrackerPartyIdentification2, False)

	@TrckrInfrmdPty.deleter
	def TrckrInfrmdPty(self):
		del self._TrckrInfrmdPty
		self._TrckrInfrmdPty = base_types.UninitialisedField(self, 'TrckrInfrmdPty', TrackerPartyIdentification2, False)

	@property
	def TrckrInfrmgPty(self):
		return self._TrckrInfrmgPty

	@TrckrInfrmgPty.setter
	def TrckrInfrmgPty(self, value):
		self._TrckrInfrmgPty = value if value is not None else base_types.UninitialisedField(self, 'TrckrInfrmgPty', TrackerPartyIdentification2, False)

	@TrckrInfrmgPty.deleter
	def TrckrInfrmgPty(self):
		del self._TrckrInfrmgPty
		self._TrckrInfrmgPty = base_types.UninitialisedField(self, 'TrckrInfrmgPty', TrackerPartyIdentification2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTrckrUpd', type=OriginalBusinessInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcLvl', type=ServiceLevel8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckrInfrmdPty', type=TrackerPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckrInfrmgPty', type=TrackerPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
	))