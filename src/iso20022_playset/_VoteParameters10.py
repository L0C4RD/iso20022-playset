# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommunicationAddress11
from . import DateFormat58Choice
from . import FinancialInstrumentQuantity18Choice
from . import IncentivePremium6
from . import Max350Text
from . import PostalAddress1
from . import VoteMethods5
from . import YesNoIndicator

class VoteParameters10(base_types._BaseFieldType):

	__slots__ = ["_AddtlDsclsrRqrmnts", "_AddtlVtngRqrmnts", "_BnfclOwnrDsclsr", "_EarlyIncntivPrm", "_EarlyVoteWthPrmDdln", "_IncntivPrm", "_PrtlVoteAllwd", "_PrvsInstrInvldtyInd", "_RvcbltyDdln", "_RvcbltyMktDdln", "_SctiesQtyReqrdToVote", "_SpltVoteAllwd", "_VoteDdln", "_VoteMktDdln", "_VoteMthds", "_VoteWthPrmDdln", "_VoteWthPrmMktDdln", "_VtngBlltElctrncAdr", "_VtngBlltReqAdr"]
	@property
	def AddtlDsclsrRqrmnts(self):
		return self._AddtlDsclsrRqrmnts

	@AddtlDsclsrRqrmnts.setter
	def AddtlDsclsrRqrmnts(self, value):
		self._AddtlDsclsrRqrmnts = value if value is not None else base_types.UninitialisedField(self, 'AddtlDsclsrRqrmnts', Max350Text, False)

	@AddtlDsclsrRqrmnts.deleter
	def AddtlDsclsrRqrmnts(self):
		del self._AddtlDsclsrRqrmnts
		self._AddtlDsclsrRqrmnts = base_types.UninitialisedField(self, 'AddtlDsclsrRqrmnts', Max350Text, False)

	@property
	def AddtlVtngRqrmnts(self):
		return self._AddtlVtngRqrmnts

	@AddtlVtngRqrmnts.setter
	def AddtlVtngRqrmnts(self, value):
		self._AddtlVtngRqrmnts = value if value is not None else base_types.UninitialisedField(self, 'AddtlVtngRqrmnts', Max350Text, False)

	@AddtlVtngRqrmnts.deleter
	def AddtlVtngRqrmnts(self):
		del self._AddtlVtngRqrmnts
		self._AddtlVtngRqrmnts = base_types.UninitialisedField(self, 'AddtlVtngRqrmnts', Max350Text, False)

	@property
	def BnfclOwnrDsclsr(self):
		return self._BnfclOwnrDsclsr

	@BnfclOwnrDsclsr.setter
	def BnfclOwnrDsclsr(self, value):
		self._BnfclOwnrDsclsr = value if value is not None else base_types.UninitialisedField(self, 'BnfclOwnrDsclsr', YesNoIndicator, False)

	@BnfclOwnrDsclsr.deleter
	def BnfclOwnrDsclsr(self):
		del self._BnfclOwnrDsclsr
		self._BnfclOwnrDsclsr = base_types.UninitialisedField(self, 'BnfclOwnrDsclsr', YesNoIndicator, False)

	@property
	def EarlyIncntivPrm(self):
		return self._EarlyIncntivPrm

	@EarlyIncntivPrm.setter
	def EarlyIncntivPrm(self, value):
		self._EarlyIncntivPrm = value if value is not None else base_types.UninitialisedField(self, 'EarlyIncntivPrm', IncentivePremium6, False)

	@EarlyIncntivPrm.deleter
	def EarlyIncntivPrm(self):
		del self._EarlyIncntivPrm
		self._EarlyIncntivPrm = base_types.UninitialisedField(self, 'EarlyIncntivPrm', IncentivePremium6, False)

	@property
	def EarlyVoteWthPrmDdln(self):
		return self._EarlyVoteWthPrmDdln

	@EarlyVoteWthPrmDdln.setter
	def EarlyVoteWthPrmDdln(self, value):
		self._EarlyVoteWthPrmDdln = value if value is not None else base_types.UninitialisedField(self, 'EarlyVoteWthPrmDdln', DateFormat58Choice, False)

	@EarlyVoteWthPrmDdln.deleter
	def EarlyVoteWthPrmDdln(self):
		del self._EarlyVoteWthPrmDdln
		self._EarlyVoteWthPrmDdln = base_types.UninitialisedField(self, 'EarlyVoteWthPrmDdln', DateFormat58Choice, False)

	@property
	def IncntivPrm(self):
		return self._IncntivPrm

	@IncntivPrm.setter
	def IncntivPrm(self, value):
		self._IncntivPrm = value if value is not None else base_types.UninitialisedField(self, 'IncntivPrm', IncentivePremium6, False)

	@IncntivPrm.deleter
	def IncntivPrm(self):
		del self._IncntivPrm
		self._IncntivPrm = base_types.UninitialisedField(self, 'IncntivPrm', IncentivePremium6, False)

	@property
	def PrtlVoteAllwd(self):
		return self._PrtlVoteAllwd

	@PrtlVoteAllwd.setter
	def PrtlVoteAllwd(self, value):
		self._PrtlVoteAllwd = value if value is not None else base_types.UninitialisedField(self, 'PrtlVoteAllwd', YesNoIndicator, False)

	@PrtlVoteAllwd.deleter
	def PrtlVoteAllwd(self):
		del self._PrtlVoteAllwd
		self._PrtlVoteAllwd = base_types.UninitialisedField(self, 'PrtlVoteAllwd', YesNoIndicator, False)

	@property
	def PrvsInstrInvldtyInd(self):
		return self._PrvsInstrInvldtyInd

	@PrvsInstrInvldtyInd.setter
	def PrvsInstrInvldtyInd(self, value):
		self._PrvsInstrInvldtyInd = value if value is not None else base_types.UninitialisedField(self, 'PrvsInstrInvldtyInd', YesNoIndicator, False)

	@PrvsInstrInvldtyInd.deleter
	def PrvsInstrInvldtyInd(self):
		del self._PrvsInstrInvldtyInd
		self._PrvsInstrInvldtyInd = base_types.UninitialisedField(self, 'PrvsInstrInvldtyInd', YesNoIndicator, False)

	@property
	def RvcbltyDdln(self):
		return self._RvcbltyDdln

	@RvcbltyDdln.setter
	def RvcbltyDdln(self, value):
		self._RvcbltyDdln = value if value is not None else base_types.UninitialisedField(self, 'RvcbltyDdln', DateFormat58Choice, False)

	@RvcbltyDdln.deleter
	def RvcbltyDdln(self):
		del self._RvcbltyDdln
		self._RvcbltyDdln = base_types.UninitialisedField(self, 'RvcbltyDdln', DateFormat58Choice, False)

	@property
	def RvcbltyMktDdln(self):
		return self._RvcbltyMktDdln

	@RvcbltyMktDdln.setter
	def RvcbltyMktDdln(self, value):
		self._RvcbltyMktDdln = value if value is not None else base_types.UninitialisedField(self, 'RvcbltyMktDdln', DateFormat58Choice, False)

	@RvcbltyMktDdln.deleter
	def RvcbltyMktDdln(self):
		del self._RvcbltyMktDdln
		self._RvcbltyMktDdln = base_types.UninitialisedField(self, 'RvcbltyMktDdln', DateFormat58Choice, False)

	@property
	def SctiesQtyReqrdToVote(self):
		return self._SctiesQtyReqrdToVote

	@SctiesQtyReqrdToVote.setter
	def SctiesQtyReqrdToVote(self, value):
		self._SctiesQtyReqrdToVote = value if value is not None else base_types.UninitialisedField(self, 'SctiesQtyReqrdToVote', FinancialInstrumentQuantity18Choice, False)

	@SctiesQtyReqrdToVote.deleter
	def SctiesQtyReqrdToVote(self):
		del self._SctiesQtyReqrdToVote
		self._SctiesQtyReqrdToVote = base_types.UninitialisedField(self, 'SctiesQtyReqrdToVote', FinancialInstrumentQuantity18Choice, False)

	@property
	def SpltVoteAllwd(self):
		return self._SpltVoteAllwd

	@SpltVoteAllwd.setter
	def SpltVoteAllwd(self, value):
		self._SpltVoteAllwd = value if value is not None else base_types.UninitialisedField(self, 'SpltVoteAllwd', YesNoIndicator, False)

	@SpltVoteAllwd.deleter
	def SpltVoteAllwd(self):
		del self._SpltVoteAllwd
		self._SpltVoteAllwd = base_types.UninitialisedField(self, 'SpltVoteAllwd', YesNoIndicator, False)

	@property
	def VoteDdln(self):
		return self._VoteDdln

	@VoteDdln.setter
	def VoteDdln(self, value):
		self._VoteDdln = value if value is not None else base_types.UninitialisedField(self, 'VoteDdln', DateFormat58Choice, False)

	@VoteDdln.deleter
	def VoteDdln(self):
		del self._VoteDdln
		self._VoteDdln = base_types.UninitialisedField(self, 'VoteDdln', DateFormat58Choice, False)

	@property
	def VoteMktDdln(self):
		return self._VoteMktDdln

	@VoteMktDdln.setter
	def VoteMktDdln(self, value):
		self._VoteMktDdln = value if value is not None else base_types.UninitialisedField(self, 'VoteMktDdln', DateFormat58Choice, False)

	@VoteMktDdln.deleter
	def VoteMktDdln(self):
		del self._VoteMktDdln
		self._VoteMktDdln = base_types.UninitialisedField(self, 'VoteMktDdln', DateFormat58Choice, False)

	@property
	def VoteMthds(self):
		return self._VoteMthds

	@VoteMthds.setter
	def VoteMthds(self, value):
		self._VoteMthds = value if value is not None else base_types.UninitialisedField(self, 'VoteMthds', VoteMethods5, False)

	@VoteMthds.deleter
	def VoteMthds(self):
		del self._VoteMthds
		self._VoteMthds = base_types.UninitialisedField(self, 'VoteMthds', VoteMethods5, False)

	@property
	def VoteWthPrmDdln(self):
		return self._VoteWthPrmDdln

	@VoteWthPrmDdln.setter
	def VoteWthPrmDdln(self, value):
		self._VoteWthPrmDdln = value if value is not None else base_types.UninitialisedField(self, 'VoteWthPrmDdln', DateFormat58Choice, False)

	@VoteWthPrmDdln.deleter
	def VoteWthPrmDdln(self):
		del self._VoteWthPrmDdln
		self._VoteWthPrmDdln = base_types.UninitialisedField(self, 'VoteWthPrmDdln', DateFormat58Choice, False)

	@property
	def VoteWthPrmMktDdln(self):
		return self._VoteWthPrmMktDdln

	@VoteWthPrmMktDdln.setter
	def VoteWthPrmMktDdln(self, value):
		self._VoteWthPrmMktDdln = value if value is not None else base_types.UninitialisedField(self, 'VoteWthPrmMktDdln', DateFormat58Choice, False)

	@VoteWthPrmMktDdln.deleter
	def VoteWthPrmMktDdln(self):
		del self._VoteWthPrmMktDdln
		self._VoteWthPrmMktDdln = base_types.UninitialisedField(self, 'VoteWthPrmMktDdln', DateFormat58Choice, False)

	@property
	def VtngBlltElctrncAdr(self):
		return self._VtngBlltElctrncAdr

	@VtngBlltElctrncAdr.setter
	def VtngBlltElctrncAdr(self, value):
		self._VtngBlltElctrncAdr = value if value is not None else base_types.UninitialisedField(self, 'VtngBlltElctrncAdr', CommunicationAddress11, False)

	@VtngBlltElctrncAdr.deleter
	def VtngBlltElctrncAdr(self):
		del self._VtngBlltElctrncAdr
		self._VtngBlltElctrncAdr = base_types.UninitialisedField(self, 'VtngBlltElctrncAdr', CommunicationAddress11, False)

	@property
	def VtngBlltReqAdr(self):
		return self._VtngBlltReqAdr

	@VtngBlltReqAdr.setter
	def VtngBlltReqAdr(self, value):
		self._VtngBlltReqAdr = value if value is not None else base_types.UninitialisedField(self, 'VtngBlltReqAdr', PostalAddress1, False)

	@VtngBlltReqAdr.deleter
	def VtngBlltReqAdr(self):
		del self._VtngBlltReqAdr
		self._VtngBlltReqAdr = base_types.UninitialisedField(self, 'VtngBlltReqAdr', PostalAddress1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlDsclsrRqrmnts', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlVtngRqrmnts', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfclOwnrDsclsr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyIncntivPrm', type=IncentivePremium6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyVoteWthPrmDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncntivPrm', type=IncentivePremium6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlVoteAllwd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstrInvldtyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvcbltyDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvcbltyMktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQtyReqrdToVote', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpltVoteAllwd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteMktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteMthds', type=VoteMethods5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteWthPrmDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteWthPrmMktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VtngBlltElctrncAdr', type=CommunicationAddress11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VtngBlltReqAdr', type=PostalAddress1, min=0, max=1, mutex_group=None, array=False),
	))