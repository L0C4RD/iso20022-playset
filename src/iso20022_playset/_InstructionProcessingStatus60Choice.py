# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptedStatus2
from . import CancelledStatus5
from . import ForwardedStatus1
from . import NoSpecifiedReason1
from . import PendingStatus3
from . import ProprietaryStatusAndReason6
from . import ReceivedByIssuerOrOfferorStatus1
from . import RejectedStatus15
from . import ReturnedStatus1

class InstructionProcessingStatus60Choice(base_types._BaseFieldType):

	__slots__ = ["_AccptdForFrthrPrcg", "_Canc", "_DfltActn", "_Fwdd", "_Pdg", "_PrtrySts", "_RcvdByIssrOrOfferr", "_Rjctd", "_Rtrd", "_StgInstr"]
	@property
	def AccptdForFrthrPrcg(self):
		return self._AccptdForFrthrPrcg

	@AccptdForFrthrPrcg.setter
	def AccptdForFrthrPrcg(self, value):
		self._AccptdForFrthrPrcg = value if value is not None else base_types.UninitialisedField(self, 'AccptdForFrthrPrcg', AcceptedStatus2, False)

	@AccptdForFrthrPrcg.deleter
	def AccptdForFrthrPrcg(self):
		del self._AccptdForFrthrPrcg
		self._AccptdForFrthrPrcg = base_types.UninitialisedField(self, 'AccptdForFrthrPrcg', AcceptedStatus2, False)

	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if value is not None else base_types.UninitialisedField(self, 'Canc', CancelledStatus5, False)

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = base_types.UninitialisedField(self, 'Canc', CancelledStatus5, False)

	@property
	def DfltActn(self):
		return self._DfltActn

	@DfltActn.setter
	def DfltActn(self, value):
		self._DfltActn = value if value is not None else base_types.UninitialisedField(self, 'DfltActn', NoSpecifiedReason1, False)

	@DfltActn.deleter
	def DfltActn(self):
		del self._DfltActn
		self._DfltActn = base_types.UninitialisedField(self, 'DfltActn', NoSpecifiedReason1, False)

	@property
	def Fwdd(self):
		return self._Fwdd

	@Fwdd.setter
	def Fwdd(self, value):
		self._Fwdd = value if value is not None else base_types.UninitialisedField(self, 'Fwdd', ForwardedStatus1, False)

	@Fwdd.deleter
	def Fwdd(self):
		del self._Fwdd
		self._Fwdd = base_types.UninitialisedField(self, 'Fwdd', ForwardedStatus1, False)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', PendingStatus3, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', PendingStatus3, False)

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if value is not None else base_types.UninitialisedField(self, 'PrtrySts', ProprietaryStatusAndReason6, False)

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = base_types.UninitialisedField(self, 'PrtrySts', ProprietaryStatusAndReason6, False)

	@property
	def RcvdByIssrOrOfferr(self):
		return self._RcvdByIssrOrOfferr

	@RcvdByIssrOrOfferr.setter
	def RcvdByIssrOrOfferr(self, value):
		self._RcvdByIssrOrOfferr = value if value is not None else base_types.UninitialisedField(self, 'RcvdByIssrOrOfferr', ReceivedByIssuerOrOfferorStatus1, False)

	@RcvdByIssrOrOfferr.deleter
	def RcvdByIssrOrOfferr(self):
		del self._RcvdByIssrOrOfferr
		self._RcvdByIssrOrOfferr = base_types.UninitialisedField(self, 'RcvdByIssrOrOfferr', ReceivedByIssuerOrOfferorStatus1, False)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectedStatus15, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectedStatus15, False)

	@property
	def Rtrd(self):
		return self._Rtrd

	@Rtrd.setter
	def Rtrd(self, value):
		self._Rtrd = value if value is not None else base_types.UninitialisedField(self, 'Rtrd', ReturnedStatus1, False)

	@Rtrd.deleter
	def Rtrd(self):
		del self._Rtrd
		self._Rtrd = base_types.UninitialisedField(self, 'Rtrd', ReturnedStatus1, False)

	@property
	def StgInstr(self):
		return self._StgInstr

	@StgInstr.setter
	def StgInstr(self, value):
		self._StgInstr = value if value is not None else base_types.UninitialisedField(self, 'StgInstr', NoSpecifiedReason1, False)

	@StgInstr.deleter
	def StgInstr(self):
		del self._StgInstr
		self._StgInstr = base_types.UninitialisedField(self, 'StgInstr', NoSpecifiedReason1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdForFrthrPrcg', type=AcceptedStatus2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancelledStatus5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DfltActn', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Fwdd', type=ForwardedStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcvdByIssrOrOfferr', type=ReceivedByIssuerOrOfferorStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus15, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rtrd', type=ReturnedStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StgInstr', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
	))