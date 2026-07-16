# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AustrianBankleitzahlIdentifier
from . import CHIPSParticipantIdentifier
from . import CHIPSUniversalIdentifier
from . import CanadianPaymentsARNIdentifier
from . import ExtensiveBranchNetworkIdentifier
from . import FedwireRoutingNumberIdentifier
from . import GermanBankleitzahlIdentifier
from . import HongKongBankIdentifier
from . import IrishNSCIdentifier
from . import ItalianDomesticIdentifier
from . import NewZealandNCCIdentifier
from . import PortugueseNCCIdentifier
from . import RussianCentralBankIdentificationCodeIdentifier
from . import SmallNetworkIdentifier
from . import SouthAfricanNCCIdentifier
from . import SpanishDomesticInterbankingIdentifier
from . import SwissBCIdentifier
from . import SwissSICIdentifier
from . import UKDomesticSortCodeIdentifier

class ClearingSystemMemberIdentification4Choice(base_types._BaseFieldType):

	__slots__ = ["_ATBLZ", "_AUBSBs", "_AUBSBx", "_CACPA", "_CHBC", "_CHSIC", "_DEBLZ", "_ESNCC", "_GBSC", "_HKNCC", "_IENSC", "_ITNCC", "_NZNCC", "_PTNCC", "_RUCB", "_USCH", "_USCHU", "_USFW", "_ZANCC"]
	@property
	def ATBLZ(self):
		return self._ATBLZ

	@ATBLZ.setter
	def ATBLZ(self, value):
		self._ATBLZ = value if value is not None else base_types.UninitialisedField(self, 'ATBLZ', AustrianBankleitzahlIdentifier, False)

	@ATBLZ.deleter
	def ATBLZ(self):
		del self._ATBLZ
		self._ATBLZ = base_types.UninitialisedField(self, 'ATBLZ', AustrianBankleitzahlIdentifier, False)

	@property
	def AUBSBs(self):
		return self._AUBSBs

	@AUBSBs.setter
	def AUBSBs(self, value):
		self._AUBSBs = value if value is not None else base_types.UninitialisedField(self, 'AUBSBs', SmallNetworkIdentifier, False)

	@AUBSBs.deleter
	def AUBSBs(self):
		del self._AUBSBs
		self._AUBSBs = base_types.UninitialisedField(self, 'AUBSBs', SmallNetworkIdentifier, False)

	@property
	def AUBSBx(self):
		return self._AUBSBx

	@AUBSBx.setter
	def AUBSBx(self, value):
		self._AUBSBx = value if value is not None else base_types.UninitialisedField(self, 'AUBSBx', ExtensiveBranchNetworkIdentifier, False)

	@AUBSBx.deleter
	def AUBSBx(self):
		del self._AUBSBx
		self._AUBSBx = base_types.UninitialisedField(self, 'AUBSBx', ExtensiveBranchNetworkIdentifier, False)

	@property
	def CACPA(self):
		return self._CACPA

	@CACPA.setter
	def CACPA(self, value):
		self._CACPA = value if value is not None else base_types.UninitialisedField(self, 'CACPA', CanadianPaymentsARNIdentifier, False)

	@CACPA.deleter
	def CACPA(self):
		del self._CACPA
		self._CACPA = base_types.UninitialisedField(self, 'CACPA', CanadianPaymentsARNIdentifier, False)

	@property
	def CHBC(self):
		return self._CHBC

	@CHBC.setter
	def CHBC(self, value):
		self._CHBC = value if value is not None else base_types.UninitialisedField(self, 'CHBC', SwissBCIdentifier, False)

	@CHBC.deleter
	def CHBC(self):
		del self._CHBC
		self._CHBC = base_types.UninitialisedField(self, 'CHBC', SwissBCIdentifier, False)

	@property
	def CHSIC(self):
		return self._CHSIC

	@CHSIC.setter
	def CHSIC(self, value):
		self._CHSIC = value if value is not None else base_types.UninitialisedField(self, 'CHSIC', SwissSICIdentifier, False)

	@CHSIC.deleter
	def CHSIC(self):
		del self._CHSIC
		self._CHSIC = base_types.UninitialisedField(self, 'CHSIC', SwissSICIdentifier, False)

	@property
	def DEBLZ(self):
		return self._DEBLZ

	@DEBLZ.setter
	def DEBLZ(self, value):
		self._DEBLZ = value if value is not None else base_types.UninitialisedField(self, 'DEBLZ', GermanBankleitzahlIdentifier, False)

	@DEBLZ.deleter
	def DEBLZ(self):
		del self._DEBLZ
		self._DEBLZ = base_types.UninitialisedField(self, 'DEBLZ', GermanBankleitzahlIdentifier, False)

	@property
	def ESNCC(self):
		return self._ESNCC

	@ESNCC.setter
	def ESNCC(self, value):
		self._ESNCC = value if value is not None else base_types.UninitialisedField(self, 'ESNCC', SpanishDomesticInterbankingIdentifier, False)

	@ESNCC.deleter
	def ESNCC(self):
		del self._ESNCC
		self._ESNCC = base_types.UninitialisedField(self, 'ESNCC', SpanishDomesticInterbankingIdentifier, False)

	@property
	def GBSC(self):
		return self._GBSC

	@GBSC.setter
	def GBSC(self, value):
		self._GBSC = value if value is not None else base_types.UninitialisedField(self, 'GBSC', UKDomesticSortCodeIdentifier, False)

	@GBSC.deleter
	def GBSC(self):
		del self._GBSC
		self._GBSC = base_types.UninitialisedField(self, 'GBSC', UKDomesticSortCodeIdentifier, False)

	@property
	def HKNCC(self):
		return self._HKNCC

	@HKNCC.setter
	def HKNCC(self, value):
		self._HKNCC = value if value is not None else base_types.UninitialisedField(self, 'HKNCC', HongKongBankIdentifier, False)

	@HKNCC.deleter
	def HKNCC(self):
		del self._HKNCC
		self._HKNCC = base_types.UninitialisedField(self, 'HKNCC', HongKongBankIdentifier, False)

	@property
	def IENSC(self):
		return self._IENSC

	@IENSC.setter
	def IENSC(self, value):
		self._IENSC = value if value is not None else base_types.UninitialisedField(self, 'IENSC', IrishNSCIdentifier, False)

	@IENSC.deleter
	def IENSC(self):
		del self._IENSC
		self._IENSC = base_types.UninitialisedField(self, 'IENSC', IrishNSCIdentifier, False)

	@property
	def ITNCC(self):
		return self._ITNCC

	@ITNCC.setter
	def ITNCC(self, value):
		self._ITNCC = value if value is not None else base_types.UninitialisedField(self, 'ITNCC', ItalianDomesticIdentifier, False)

	@ITNCC.deleter
	def ITNCC(self):
		del self._ITNCC
		self._ITNCC = base_types.UninitialisedField(self, 'ITNCC', ItalianDomesticIdentifier, False)

	@property
	def NZNCC(self):
		return self._NZNCC

	@NZNCC.setter
	def NZNCC(self, value):
		self._NZNCC = value if value is not None else base_types.UninitialisedField(self, 'NZNCC', NewZealandNCCIdentifier, False)

	@NZNCC.deleter
	def NZNCC(self):
		del self._NZNCC
		self._NZNCC = base_types.UninitialisedField(self, 'NZNCC', NewZealandNCCIdentifier, False)

	@property
	def PTNCC(self):
		return self._PTNCC

	@PTNCC.setter
	def PTNCC(self, value):
		self._PTNCC = value if value is not None else base_types.UninitialisedField(self, 'PTNCC', PortugueseNCCIdentifier, False)

	@PTNCC.deleter
	def PTNCC(self):
		del self._PTNCC
		self._PTNCC = base_types.UninitialisedField(self, 'PTNCC', PortugueseNCCIdentifier, False)

	@property
	def RUCB(self):
		return self._RUCB

	@RUCB.setter
	def RUCB(self, value):
		self._RUCB = value if value is not None else base_types.UninitialisedField(self, 'RUCB', RussianCentralBankIdentificationCodeIdentifier, False)

	@RUCB.deleter
	def RUCB(self):
		del self._RUCB
		self._RUCB = base_types.UninitialisedField(self, 'RUCB', RussianCentralBankIdentificationCodeIdentifier, False)

	@property
	def USCH(self):
		return self._USCH

	@USCH.setter
	def USCH(self, value):
		self._USCH = value if value is not None else base_types.UninitialisedField(self, 'USCH', CHIPSParticipantIdentifier, False)

	@USCH.deleter
	def USCH(self):
		del self._USCH
		self._USCH = base_types.UninitialisedField(self, 'USCH', CHIPSParticipantIdentifier, False)

	@property
	def USCHU(self):
		return self._USCHU

	@USCHU.setter
	def USCHU(self, value):
		self._USCHU = value if value is not None else base_types.UninitialisedField(self, 'USCHU', CHIPSUniversalIdentifier, False)

	@USCHU.deleter
	def USCHU(self):
		del self._USCHU
		self._USCHU = base_types.UninitialisedField(self, 'USCHU', CHIPSUniversalIdentifier, False)

	@property
	def USFW(self):
		return self._USFW

	@USFW.setter
	def USFW(self, value):
		self._USFW = value if value is not None else base_types.UninitialisedField(self, 'USFW', FedwireRoutingNumberIdentifier, False)

	@USFW.deleter
	def USFW(self):
		del self._USFW
		self._USFW = base_types.UninitialisedField(self, 'USFW', FedwireRoutingNumberIdentifier, False)

	@property
	def ZANCC(self):
		return self._ZANCC

	@ZANCC.setter
	def ZANCC(self, value):
		self._ZANCC = value if value is not None else base_types.UninitialisedField(self, 'ZANCC', SouthAfricanNCCIdentifier, False)

	@ZANCC.deleter
	def ZANCC(self):
		del self._ZANCC
		self._ZANCC = base_types.UninitialisedField(self, 'ZANCC', SouthAfricanNCCIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATBLZ', type=AustrianBankleitzahlIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AUBSBs', type=SmallNetworkIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AUBSBx', type=ExtensiveBranchNetworkIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CACPA', type=CanadianPaymentsARNIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CHBC', type=SwissBCIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CHSIC', type=SwissSICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DEBLZ', type=GermanBankleitzahlIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ESNCC', type=SpanishDomesticInterbankingIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='GBSC', type=UKDomesticSortCodeIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='HKNCC', type=HongKongBankIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IENSC', type=IrishNSCIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ITNCC', type=ItalianDomesticIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NZNCC', type=NewZealandNCCIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PTNCC', type=PortugueseNCCIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RUCB', type=RussianCentralBankIdentificationCodeIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='USCH', type=CHIPSParticipantIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='USCHU', type=CHIPSUniversalIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='USFW', type=FedwireRoutingNumberIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ZANCC', type=SouthAfricanNCCIdentifier, min=0, max=1, mutex_group=1, array=False),
	))