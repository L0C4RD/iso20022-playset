from . import base_types
from .IncentivePremium6 import IncentivePremium6
from .YesNoIndicator import YesNoIndicator
from .PostalAddress1 import PostalAddress1
from .Max350Text import Max350Text
from .VoteMethods5 import VoteMethods5
from .CommunicationAddress11 import CommunicationAddress11
from .FinancialInstrumentQuantity18Choice import FinancialInstrumentQuantity18Choice
from .DateFormat58Choice import DateFormat58Choice

class VoteParameters9(base_types._BaseFieldType):

	__slots__ = ["_IncntivPrm", "_RvcbltyDdln", "_AddtlVtngRqrmnts", "_PrtlVoteAllwd", "_VoteWthPrmDdln", "_RvcbltyMktDdln", "_VoteDdln", "_EarlyIncntivPrm", "_VoteWthPrmMktDdln", "_VoteMktDdln", "_VoteMthds", "_EarlyVoteWthPrmDdln", "_VtngBlltElctrncAdr", "_PrvsInstrInvldtyInd", "_SctiesQtyReqrdToVote", "_BnfclOwnrDsclsr", "_VtngBlltReqAdr", "_SpltVoteAllwd"]
	@property
	def IncntivPrm(self):
		return self._IncntivPrm

	@IncntivPrm.setter
	def IncntivPrm(self, value):
		self._IncntivPrm = value if type(value) != auto else self.make_default("IncntivPrm")

	@IncntivPrm.deleter
	def IncntivPrm(self):
		del self._IncntivPrm
		self._IncntivPrm = None

	@property
	def RvcbltyDdln(self):
		return self._RvcbltyDdln

	@RvcbltyDdln.setter
	def RvcbltyDdln(self, value):
		self._RvcbltyDdln = value if type(value) != auto else self.make_default("RvcbltyDdln")

	@RvcbltyDdln.deleter
	def RvcbltyDdln(self):
		del self._RvcbltyDdln
		self._RvcbltyDdln = None

	@property
	def AddtlVtngRqrmnts(self):
		return self._AddtlVtngRqrmnts

	@AddtlVtngRqrmnts.setter
	def AddtlVtngRqrmnts(self, value):
		self._AddtlVtngRqrmnts = value if type(value) != auto else self.make_default("AddtlVtngRqrmnts")

	@AddtlVtngRqrmnts.deleter
	def AddtlVtngRqrmnts(self):
		del self._AddtlVtngRqrmnts
		self._AddtlVtngRqrmnts = None

	@property
	def PrtlVoteAllwd(self):
		return self._PrtlVoteAllwd

	@PrtlVoteAllwd.setter
	def PrtlVoteAllwd(self, value):
		self._PrtlVoteAllwd = value if type(value) != auto else self.make_default("PrtlVoteAllwd")

	@PrtlVoteAllwd.deleter
	def PrtlVoteAllwd(self):
		del self._PrtlVoteAllwd
		self._PrtlVoteAllwd = None

	@property
	def VoteWthPrmDdln(self):
		return self._VoteWthPrmDdln

	@VoteWthPrmDdln.setter
	def VoteWthPrmDdln(self, value):
		self._VoteWthPrmDdln = value if type(value) != auto else self.make_default("VoteWthPrmDdln")

	@VoteWthPrmDdln.deleter
	def VoteWthPrmDdln(self):
		del self._VoteWthPrmDdln
		self._VoteWthPrmDdln = None

	@property
	def RvcbltyMktDdln(self):
		return self._RvcbltyMktDdln

	@RvcbltyMktDdln.setter
	def RvcbltyMktDdln(self, value):
		self._RvcbltyMktDdln = value if type(value) != auto else self.make_default("RvcbltyMktDdln")

	@RvcbltyMktDdln.deleter
	def RvcbltyMktDdln(self):
		del self._RvcbltyMktDdln
		self._RvcbltyMktDdln = None

	@property
	def VoteDdln(self):
		return self._VoteDdln

	@VoteDdln.setter
	def VoteDdln(self, value):
		self._VoteDdln = value if type(value) != auto else self.make_default("VoteDdln")

	@VoteDdln.deleter
	def VoteDdln(self):
		del self._VoteDdln
		self._VoteDdln = None

	@property
	def EarlyIncntivPrm(self):
		return self._EarlyIncntivPrm

	@EarlyIncntivPrm.setter
	def EarlyIncntivPrm(self, value):
		self._EarlyIncntivPrm = value if type(value) != auto else self.make_default("EarlyIncntivPrm")

	@EarlyIncntivPrm.deleter
	def EarlyIncntivPrm(self):
		del self._EarlyIncntivPrm
		self._EarlyIncntivPrm = None

	@property
	def VoteWthPrmMktDdln(self):
		return self._VoteWthPrmMktDdln

	@VoteWthPrmMktDdln.setter
	def VoteWthPrmMktDdln(self, value):
		self._VoteWthPrmMktDdln = value if type(value) != auto else self.make_default("VoteWthPrmMktDdln")

	@VoteWthPrmMktDdln.deleter
	def VoteWthPrmMktDdln(self):
		del self._VoteWthPrmMktDdln
		self._VoteWthPrmMktDdln = None

	@property
	def VoteMktDdln(self):
		return self._VoteMktDdln

	@VoteMktDdln.setter
	def VoteMktDdln(self, value):
		self._VoteMktDdln = value if type(value) != auto else self.make_default("VoteMktDdln")

	@VoteMktDdln.deleter
	def VoteMktDdln(self):
		del self._VoteMktDdln
		self._VoteMktDdln = None

	@property
	def VoteMthds(self):
		return self._VoteMthds

	@VoteMthds.setter
	def VoteMthds(self, value):
		self._VoteMthds = value if type(value) != auto else self.make_default("VoteMthds")

	@VoteMthds.deleter
	def VoteMthds(self):
		del self._VoteMthds
		self._VoteMthds = None

	@property
	def EarlyVoteWthPrmDdln(self):
		return self._EarlyVoteWthPrmDdln

	@EarlyVoteWthPrmDdln.setter
	def EarlyVoteWthPrmDdln(self, value):
		self._EarlyVoteWthPrmDdln = value if type(value) != auto else self.make_default("EarlyVoteWthPrmDdln")

	@EarlyVoteWthPrmDdln.deleter
	def EarlyVoteWthPrmDdln(self):
		del self._EarlyVoteWthPrmDdln
		self._EarlyVoteWthPrmDdln = None

	@property
	def VtngBlltElctrncAdr(self):
		return self._VtngBlltElctrncAdr

	@VtngBlltElctrncAdr.setter
	def VtngBlltElctrncAdr(self, value):
		self._VtngBlltElctrncAdr = value if type(value) != auto else self.make_default("VtngBlltElctrncAdr")

	@VtngBlltElctrncAdr.deleter
	def VtngBlltElctrncAdr(self):
		del self._VtngBlltElctrncAdr
		self._VtngBlltElctrncAdr = None

	@property
	def PrvsInstrInvldtyInd(self):
		return self._PrvsInstrInvldtyInd

	@PrvsInstrInvldtyInd.setter
	def PrvsInstrInvldtyInd(self, value):
		self._PrvsInstrInvldtyInd = value if type(value) != auto else self.make_default("PrvsInstrInvldtyInd")

	@PrvsInstrInvldtyInd.deleter
	def PrvsInstrInvldtyInd(self):
		del self._PrvsInstrInvldtyInd
		self._PrvsInstrInvldtyInd = None

	@property
	def SctiesQtyReqrdToVote(self):
		return self._SctiesQtyReqrdToVote

	@SctiesQtyReqrdToVote.setter
	def SctiesQtyReqrdToVote(self, value):
		self._SctiesQtyReqrdToVote = value if type(value) != auto else self.make_default("SctiesQtyReqrdToVote")

	@SctiesQtyReqrdToVote.deleter
	def SctiesQtyReqrdToVote(self):
		del self._SctiesQtyReqrdToVote
		self._SctiesQtyReqrdToVote = None

	@property
	def BnfclOwnrDsclsr(self):
		return self._BnfclOwnrDsclsr

	@BnfclOwnrDsclsr.setter
	def BnfclOwnrDsclsr(self, value):
		self._BnfclOwnrDsclsr = value if type(value) != auto else self.make_default("BnfclOwnrDsclsr")

	@BnfclOwnrDsclsr.deleter
	def BnfclOwnrDsclsr(self):
		del self._BnfclOwnrDsclsr
		self._BnfclOwnrDsclsr = None

	@property
	def VtngBlltReqAdr(self):
		return self._VtngBlltReqAdr

	@VtngBlltReqAdr.setter
	def VtngBlltReqAdr(self, value):
		self._VtngBlltReqAdr = value if type(value) != auto else self.make_default("VtngBlltReqAdr")

	@VtngBlltReqAdr.deleter
	def VtngBlltReqAdr(self):
		del self._VtngBlltReqAdr
		self._VtngBlltReqAdr = None

	@property
	def SpltVoteAllwd(self):
		return self._SpltVoteAllwd

	@SpltVoteAllwd.setter
	def SpltVoteAllwd(self, value):
		self._SpltVoteAllwd = value if type(value) != auto else self.make_default("SpltVoteAllwd")

	@SpltVoteAllwd.deleter
	def SpltVoteAllwd(self):
		del self._SpltVoteAllwd
		self._SpltVoteAllwd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IncntivPrm', type=IncentivePremium6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvcbltyDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlVtngRqrmnts', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlVoteAllwd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteWthPrmDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvcbltyMktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyIncntivPrm', type=IncentivePremium6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteWthPrmMktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteMktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteMthds', type=VoteMethods5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyVoteWthPrmDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VtngBlltElctrncAdr', type=CommunicationAddress11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstrInvldtyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQtyReqrdToVote', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfclOwnrDsclsr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VtngBlltReqAdr', type=PostalAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpltVoteAllwd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

