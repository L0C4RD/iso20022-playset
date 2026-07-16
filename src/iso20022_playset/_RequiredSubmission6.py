# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICIdentification1
from . import Exact4AlphaNumericText
from . import Max140Text

class RequiredSubmission6(base_types._BaseFieldType):

	__slots__ = ["_CertTp", "_CertTpDesc", "_Submitr"]
	@property
	def CertTp(self):
		return self._CertTp

	@CertTp.setter
	def CertTp(self, value):
		self._CertTp = value if value is not None else base_types.UninitialisedField(self, 'CertTp', Exact4AlphaNumericText, False)

	@CertTp.deleter
	def CertTp(self):
		del self._CertTp
		self._CertTp = base_types.UninitialisedField(self, 'CertTp', Exact4AlphaNumericText, False)

	@property
	def CertTpDesc(self):
		return self._CertTpDesc

	@CertTpDesc.setter
	def CertTpDesc(self, value):
		self._CertTpDesc = value if value is not None else base_types.UninitialisedField(self, 'CertTpDesc', Max140Text, False)

	@CertTpDesc.deleter
	def CertTpDesc(self):
		del self._CertTpDesc
		self._CertTpDesc = base_types.UninitialisedField(self, 'CertTpDesc', Max140Text, False)

	@property
	def Submitr(self):
		return self._Submitr

	@Submitr.setter
	def Submitr(self, value):
		self._Submitr = value if value is not None else base_types.UninitialisedField(self, 'Submitr', BICIdentification1, True)

	@Submitr.deleter
	def Submitr(self):
		del self._Submitr
		self._Submitr = base_types.UninitialisedField(self, 'Submitr', BICIdentification1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertTp', type=Exact4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertTpDesc', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Submitr', type=BICIdentification1, min=1, max=None, mutex_group=None, array=True),
	))