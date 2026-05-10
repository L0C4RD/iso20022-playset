from . import base_types
from ._CanadianPaymentsARNIdentifier import CanadianPaymentsARNIdentifier
from ._PortugueseNCCIdentifier import PortugueseNCCIdentifier
from ._SwissSICIdentifier import SwissSICIdentifier
from ._SmallNetworkIdentifier import SmallNetworkIdentifier
from ._SwissBCIdentifier import SwissBCIdentifier
from ._SouthAfricanNCCIdentifier import SouthAfricanNCCIdentifier
from ._ExtensiveBranchNetworkIdentifier import ExtensiveBranchNetworkIdentifier
from ._AustrianBankleitzahlIdentifier import AustrianBankleitzahlIdentifier
from ._RussianCentralBankIdentificationCodeIdentifier import RussianCentralBankIdentificationCodeIdentifier
from ._NewZealandNCCIdentifier import NewZealandNCCIdentifier
from ._FedwireRoutingNumberIdentifier import FedwireRoutingNumberIdentifier
from ._GermanBankleitzahlIdentifier import GermanBankleitzahlIdentifier
from ._IrishNSCIdentifier import IrishNSCIdentifier
from ._CHIPSParticipantIdentifier import CHIPSParticipantIdentifier
from ._ItalianDomesticIdentifier import ItalianDomesticIdentifier
from ._HongKongBankIdentifier import HongKongBankIdentifier
from ._CHIPSUniversalIdentifier import CHIPSUniversalIdentifier
from ._UKDomesticSortCodeIdentifier import UKDomesticSortCodeIdentifier
from ._SpanishDomesticInterbankingIdentifier import SpanishDomesticInterbankingIdentifier

class ClearingSystemMemberIdentification4Choice(base_types._BaseFieldType):

	__slots__ = ["_AUBSBs", "_ITNCC", "_ZANCC", "_PTNCC", "_RUCB", "_GBSC", "_CHBC", "_AUBSBx", "_USCHU", "_HKNCC", "_USCH", "_IENSC", "_ATBLZ", "_ESNCC", "_CHSIC", "_CACPA", "_NZNCC", "_USFW", "_DEBLZ"]
	@property
	def ATBLZ(self):
		return self._ATBLZ

	@ATBLZ.setter
	def ATBLZ(self, value):
		self._ATBLZ = value if type(value) != base_types.auto else self.make_default("ATBLZ")

	@ATBLZ.deleter
	def ATBLZ(self):
		del self._ATBLZ
		self._ATBLZ = None

	@property
	def AUBSBs(self):
		return self._AUBSBs

	@AUBSBs.setter
	def AUBSBs(self, value):
		self._AUBSBs = value if type(value) != base_types.auto else self.make_default("AUBSBs")

	@AUBSBs.deleter
	def AUBSBs(self):
		del self._AUBSBs
		self._AUBSBs = None

	@property
	def AUBSBx(self):
		return self._AUBSBx

	@AUBSBx.setter
	def AUBSBx(self, value):
		self._AUBSBx = value if type(value) != base_types.auto else self.make_default("AUBSBx")

	@AUBSBx.deleter
	def AUBSBx(self):
		del self._AUBSBx
		self._AUBSBx = None

	@property
	def CACPA(self):
		return self._CACPA

	@CACPA.setter
	def CACPA(self, value):
		self._CACPA = value if type(value) != base_types.auto else self.make_default("CACPA")

	@CACPA.deleter
	def CACPA(self):
		del self._CACPA
		self._CACPA = None

	@property
	def CHBC(self):
		return self._CHBC

	@CHBC.setter
	def CHBC(self, value):
		self._CHBC = value if type(value) != base_types.auto else self.make_default("CHBC")

	@CHBC.deleter
	def CHBC(self):
		del self._CHBC
		self._CHBC = None

	@property
	def CHSIC(self):
		return self._CHSIC

	@CHSIC.setter
	def CHSIC(self, value):
		self._CHSIC = value if type(value) != base_types.auto else self.make_default("CHSIC")

	@CHSIC.deleter
	def CHSIC(self):
		del self._CHSIC
		self._CHSIC = None

	@property
	def DEBLZ(self):
		return self._DEBLZ

	@DEBLZ.setter
	def DEBLZ(self, value):
		self._DEBLZ = value if type(value) != base_types.auto else self.make_default("DEBLZ")

	@DEBLZ.deleter
	def DEBLZ(self):
		del self._DEBLZ
		self._DEBLZ = None

	@property
	def ESNCC(self):
		return self._ESNCC

	@ESNCC.setter
	def ESNCC(self, value):
		self._ESNCC = value if type(value) != base_types.auto else self.make_default("ESNCC")

	@ESNCC.deleter
	def ESNCC(self):
		del self._ESNCC
		self._ESNCC = None

	@property
	def GBSC(self):
		return self._GBSC

	@GBSC.setter
	def GBSC(self, value):
		self._GBSC = value if type(value) != base_types.auto else self.make_default("GBSC")

	@GBSC.deleter
	def GBSC(self):
		del self._GBSC
		self._GBSC = None

	@property
	def HKNCC(self):
		return self._HKNCC

	@HKNCC.setter
	def HKNCC(self, value):
		self._HKNCC = value if type(value) != base_types.auto else self.make_default("HKNCC")

	@HKNCC.deleter
	def HKNCC(self):
		del self._HKNCC
		self._HKNCC = None

	@property
	def IENSC(self):
		return self._IENSC

	@IENSC.setter
	def IENSC(self, value):
		self._IENSC = value if type(value) != base_types.auto else self.make_default("IENSC")

	@IENSC.deleter
	def IENSC(self):
		del self._IENSC
		self._IENSC = None

	@property
	def ITNCC(self):
		return self._ITNCC

	@ITNCC.setter
	def ITNCC(self, value):
		self._ITNCC = value if type(value) != base_types.auto else self.make_default("ITNCC")

	@ITNCC.deleter
	def ITNCC(self):
		del self._ITNCC
		self._ITNCC = None

	@property
	def NZNCC(self):
		return self._NZNCC

	@NZNCC.setter
	def NZNCC(self, value):
		self._NZNCC = value if type(value) != base_types.auto else self.make_default("NZNCC")

	@NZNCC.deleter
	def NZNCC(self):
		del self._NZNCC
		self._NZNCC = None

	@property
	def PTNCC(self):
		return self._PTNCC

	@PTNCC.setter
	def PTNCC(self, value):
		self._PTNCC = value if type(value) != base_types.auto else self.make_default("PTNCC")

	@PTNCC.deleter
	def PTNCC(self):
		del self._PTNCC
		self._PTNCC = None

	@property
	def RUCB(self):
		return self._RUCB

	@RUCB.setter
	def RUCB(self, value):
		self._RUCB = value if type(value) != base_types.auto else self.make_default("RUCB")

	@RUCB.deleter
	def RUCB(self):
		del self._RUCB
		self._RUCB = None

	@property
	def USCH(self):
		return self._USCH

	@USCH.setter
	def USCH(self, value):
		self._USCH = value if type(value) != base_types.auto else self.make_default("USCH")

	@USCH.deleter
	def USCH(self):
		del self._USCH
		self._USCH = None

	@property
	def USCHU(self):
		return self._USCHU

	@USCHU.setter
	def USCHU(self, value):
		self._USCHU = value if type(value) != base_types.auto else self.make_default("USCHU")

	@USCHU.deleter
	def USCHU(self):
		del self._USCHU
		self._USCHU = None

	@property
	def USFW(self):
		return self._USFW

	@USFW.setter
	def USFW(self, value):
		self._USFW = value if type(value) != base_types.auto else self.make_default("USFW")

	@USFW.deleter
	def USFW(self):
		del self._USFW
		self._USFW = None

	@property
	def ZANCC(self):
		return self._ZANCC

	@ZANCC.setter
	def ZANCC(self, value):
		self._ZANCC = value if type(value) != base_types.auto else self.make_default("ZANCC")

	@ZANCC.deleter
	def ZANCC(self):
		del self._ZANCC
		self._ZANCC = None

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

