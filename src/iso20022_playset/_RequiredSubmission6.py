from . import base_types
from ._BICIdentification1 import BICIdentification1
from ._Exact4AlphaNumericText import Exact4AlphaNumericText
from ._Max140Text import Max140Text

class RequiredSubmission6(base_types._BaseFieldType):

	__slots__ = ["_CertTp", "_CertTpDesc", "_Submitr"]
	@property
	def CertTp(self):
		return self._CertTp

	@CertTp.setter
	def CertTp(self, value):
		self._CertTp = value if type(value) != base_types.auto else self.make_default("CertTp")

	@CertTp.deleter
	def CertTp(self):
		del self._CertTp
		self._CertTp = None

	@property
	def CertTpDesc(self):
		return self._CertTpDesc

	@CertTpDesc.setter
	def CertTpDesc(self, value):
		self._CertTpDesc = value if type(value) != base_types.auto else self.make_default("CertTpDesc")

	@CertTpDesc.deleter
	def CertTpDesc(self):
		del self._CertTpDesc
		self._CertTpDesc = None

	@property
	def Submitr(self):
		return self._Submitr

	@Submitr.setter
	def Submitr(self, value):
		self._Submitr = value if type(value) != base_types.auto else self.make_default("Submitr")

	@Submitr.deleter
	def Submitr(self):
		del self._Submitr
		self._Submitr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertTp', type=Exact4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertTpDesc', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Submitr', type=BICIdentification1, min=1, max=None, mutex_group=None, array=True),
	))

