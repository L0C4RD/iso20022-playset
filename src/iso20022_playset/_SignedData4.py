# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlgorithmIdentification16
from . import EncapsulatedContent3
from . import Max5000Binary
from . import Number
from . import Signer3

class SignedData4(base_types._BaseFieldType):

	__slots__ = ["_Cert", "_DgstAlgo", "_NcpsltdCntt", "_Sgnr", "_Vrsn"]
	@property
	def Cert(self):
		return self._Cert

	@Cert.setter
	def Cert(self, value):
		self._Cert = value if value is not None else base_types.UninitialisedField(self, 'Cert', Max5000Binary, True)

	@Cert.deleter
	def Cert(self):
		del self._Cert
		self._Cert = base_types.UninitialisedField(self, 'Cert', Max5000Binary, True)

	@property
	def DgstAlgo(self):
		return self._DgstAlgo

	@DgstAlgo.setter
	def DgstAlgo(self, value):
		self._DgstAlgo = value if value is not None else base_types.UninitialisedField(self, 'DgstAlgo', AlgorithmIdentification16, True)

	@DgstAlgo.deleter
	def DgstAlgo(self):
		del self._DgstAlgo
		self._DgstAlgo = base_types.UninitialisedField(self, 'DgstAlgo', AlgorithmIdentification16, True)

	@property
	def NcpsltdCntt(self):
		return self._NcpsltdCntt

	@NcpsltdCntt.setter
	def NcpsltdCntt(self, value):
		self._NcpsltdCntt = value if value is not None else base_types.UninitialisedField(self, 'NcpsltdCntt', EncapsulatedContent3, False)

	@NcpsltdCntt.deleter
	def NcpsltdCntt(self):
		del self._NcpsltdCntt
		self._NcpsltdCntt = base_types.UninitialisedField(self, 'NcpsltdCntt', EncapsulatedContent3, False)

	@property
	def Sgnr(self):
		return self._Sgnr

	@Sgnr.setter
	def Sgnr(self, value):
		self._Sgnr = value if value is not None else base_types.UninitialisedField(self, 'Sgnr', Signer3, True)

	@Sgnr.deleter
	def Sgnr(self):
		del self._Sgnr
		self._Sgnr = base_types.UninitialisedField(self, 'Sgnr', Signer3, True)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Number, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cert', type=Max5000Binary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DgstAlgo', type=AlgorithmIdentification16, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NcpsltdCntt', type=EncapsulatedContent3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgnr', type=Signer3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
	))