# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Algorithm26Code import Algorithm26Code
from ._AlgorithmIdentification34 import AlgorithmIdentification34
from ._Max140Text import Max140Text
from ._Number import Number

class Parameter16(base_types._BaseFieldType):

	__slots__ = ["_DgstAlgo", "_MskGnrtrAlgo", "_OIDCrvNm", "_SaltLngth", "_TrlrFld"]
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
	def MskGnrtrAlgo(self):
		return self._MskGnrtrAlgo

	@MskGnrtrAlgo.setter
	def MskGnrtrAlgo(self, value):
		self._MskGnrtrAlgo = value if type(value) != base_types.auto else self.make_default("MskGnrtrAlgo")

	@MskGnrtrAlgo.deleter
	def MskGnrtrAlgo(self):
		del self._MskGnrtrAlgo
		self._MskGnrtrAlgo = None

	@property
	def OIDCrvNm(self):
		return self._OIDCrvNm

	@OIDCrvNm.setter
	def OIDCrvNm(self, value):
		self._OIDCrvNm = value if type(value) != base_types.auto else self.make_default("OIDCrvNm")

	@OIDCrvNm.deleter
	def OIDCrvNm(self):
		del self._OIDCrvNm
		self._OIDCrvNm = None

	@property
	def SaltLngth(self):
		return self._SaltLngth

	@SaltLngth.setter
	def SaltLngth(self, value):
		self._SaltLngth = value if type(value) != base_types.auto else self.make_default("SaltLngth")

	@SaltLngth.deleter
	def SaltLngth(self):
		del self._SaltLngth
		self._SaltLngth = None

	@property
	def TrlrFld(self):
		return self._TrlrFld

	@TrlrFld.setter
	def TrlrFld(self, value):
		self._TrlrFld = value if type(value) != base_types.auto else self.make_default("TrlrFld")

	@TrlrFld.deleter
	def TrlrFld(self):
		del self._TrlrFld
		self._TrlrFld = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgstAlgo', type=Algorithm26Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MskGnrtrAlgo', type=AlgorithmIdentification34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OIDCrvNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaltLngth', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrlrFld', type=Number, min=0, max=1, mutex_group=None, array=False),
	))