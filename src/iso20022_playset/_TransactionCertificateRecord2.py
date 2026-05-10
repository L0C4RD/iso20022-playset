from . import base_types
from ._DocumentGeneralInformation5 import DocumentGeneralInformation5
from ._Exact1NumericText import Exact1NumericText
from ._Max35Text import Max35Text
from ._TransactionCertificate5 import TransactionCertificate5
from ._TransactionCertificateContract2 import TransactionCertificateContract2

class TransactionCertificateRecord2(base_types._BaseFieldType):

	__slots__ = ["_Attchmnt", "_CertRcrdId", "_Ctrct", "_DocSubmitgPrcdr", "_Tx"]
	@property
	def Attchmnt(self):
		return self._Attchmnt

	@Attchmnt.setter
	def Attchmnt(self, value):
		self._Attchmnt = value if type(value) != base_types.auto else self.make_default("Attchmnt")

	@Attchmnt.deleter
	def Attchmnt(self):
		del self._Attchmnt
		self._Attchmnt = None

	@property
	def CertRcrdId(self):
		return self._CertRcrdId

	@CertRcrdId.setter
	def CertRcrdId(self, value):
		self._CertRcrdId = value if type(value) != base_types.auto else self.make_default("CertRcrdId")

	@CertRcrdId.deleter
	def CertRcrdId(self):
		del self._CertRcrdId
		self._CertRcrdId = None

	@property
	def Ctrct(self):
		return self._Ctrct

	@Ctrct.setter
	def Ctrct(self, value):
		self._Ctrct = value if type(value) != base_types.auto else self.make_default("Ctrct")

	@Ctrct.deleter
	def Ctrct(self):
		del self._Ctrct
		self._Ctrct = None

	@property
	def DocSubmitgPrcdr(self):
		return self._DocSubmitgPrcdr

	@DocSubmitgPrcdr.setter
	def DocSubmitgPrcdr(self, value):
		self._DocSubmitgPrcdr = value if type(value) != base_types.auto else self.make_default("DocSubmitgPrcdr")

	@DocSubmitgPrcdr.deleter
	def DocSubmitgPrcdr(self):
		del self._DocSubmitgPrcdr
		self._DocSubmitgPrcdr = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != base_types.auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Attchmnt', type=DocumentGeneralInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CertRcrdId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctrct', type=TransactionCertificateContract2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocSubmitgPrcdr', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=TransactionCertificate5, min=1, max=1, mutex_group=None, array=False),
	))

