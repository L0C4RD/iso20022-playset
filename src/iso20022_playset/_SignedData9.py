# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AlgorithmIdentification36 import AlgorithmIdentification36
from ._EncapsulatedContent3 import EncapsulatedContent3
from ._Max5000Binary import Max5000Binary
from ._Number import Number
from ._Signer8 import Signer8

class SignedData9(base_types._BaseFieldType):

	__slots__ = ["_Cert", "_DgstAlgo", "_NcpsltdCntt", "_Sgnr", "_Vrsn"]
	@property
	def Cert(self):
		return self._Cert

	@Cert.setter
	def Cert(self, value):
		self._Cert = value if type(value) != base_types.auto else self.make_default("Cert")

	@Cert.deleter
	def Cert(self):
		del self._Cert
		self._Cert = None

	@property
	def DgstAlgo(self):
		return self._DgstAlgo

	@DgstAlgo.setter
	def DgstAlgo(self, value):
		self._DgstAlgo = value if type(value) != base_types.auto else self.make_default("DgstAlgo")

	@DgstAlgo.deleter
	def DgstAlgo(self):
		del self._DgstAlgo
		self._DgstAlgo = None

	@property
	def NcpsltdCntt(self):
		return self._NcpsltdCntt

	@NcpsltdCntt.setter
	def NcpsltdCntt(self, value):
		self._NcpsltdCntt = value if type(value) != base_types.auto else self.make_default("NcpsltdCntt")

	@NcpsltdCntt.deleter
	def NcpsltdCntt(self):
		del self._NcpsltdCntt
		self._NcpsltdCntt = None

	@property
	def Sgnr(self):
		return self._Sgnr

	@Sgnr.setter
	def Sgnr(self, value):
		self._Sgnr = value if type(value) != base_types.auto else self.make_default("Sgnr")

	@Sgnr.deleter
	def Sgnr(self):
		del self._Sgnr
		self._Sgnr = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != base_types.auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cert', type=Max5000Binary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DgstAlgo', type=AlgorithmIdentification36, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NcpsltdCntt', type=EncapsulatedContent3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgnr', type=Signer8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
	))