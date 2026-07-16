# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentGeneralInformation5
from . import Exact1NumericText
from . import Max35Text
from . import TransactionCertificate5
from . import TransactionCertificateContract2

class TransactionCertificateRecord2(base_types._BaseFieldType):

	__slots__ = ["_Attchmnt", "_CertRcrdId", "_Ctrct", "_DocSubmitgPrcdr", "_Tx"]
	@property
	def Attchmnt(self):
		return self._Attchmnt

	@Attchmnt.setter
	def Attchmnt(self, value):
		self._Attchmnt = value if value is not None else base_types.UninitialisedField(self, 'Attchmnt', DocumentGeneralInformation5, True)

	@Attchmnt.deleter
	def Attchmnt(self):
		del self._Attchmnt
		self._Attchmnt = base_types.UninitialisedField(self, 'Attchmnt', DocumentGeneralInformation5, True)

	@property
	def CertRcrdId(self):
		return self._CertRcrdId

	@CertRcrdId.setter
	def CertRcrdId(self, value):
		self._CertRcrdId = value if value is not None else base_types.UninitialisedField(self, 'CertRcrdId', Max35Text, False)

	@CertRcrdId.deleter
	def CertRcrdId(self):
		del self._CertRcrdId
		self._CertRcrdId = base_types.UninitialisedField(self, 'CertRcrdId', Max35Text, False)

	@property
	def Ctrct(self):
		return self._Ctrct

	@Ctrct.setter
	def Ctrct(self, value):
		self._Ctrct = value if value is not None else base_types.UninitialisedField(self, 'Ctrct', TransactionCertificateContract2, False)

	@Ctrct.deleter
	def Ctrct(self):
		del self._Ctrct
		self._Ctrct = base_types.UninitialisedField(self, 'Ctrct', TransactionCertificateContract2, False)

	@property
	def DocSubmitgPrcdr(self):
		return self._DocSubmitgPrcdr

	@DocSubmitgPrcdr.setter
	def DocSubmitgPrcdr(self, value):
		self._DocSubmitgPrcdr = value if value is not None else base_types.UninitialisedField(self, 'DocSubmitgPrcdr', Exact1NumericText, False)

	@DocSubmitgPrcdr.deleter
	def DocSubmitgPrcdr(self):
		del self._DocSubmitgPrcdr
		self._DocSubmitgPrcdr = base_types.UninitialisedField(self, 'DocSubmitgPrcdr', Exact1NumericText, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', TransactionCertificate5, False)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', TransactionCertificate5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Attchmnt', type=DocumentGeneralInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CertRcrdId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctrct', type=TransactionCertificateContract2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocSubmitgPrcdr', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=TransactionCertificate5, min=1, max=1, mutex_group=None, array=False),
	))