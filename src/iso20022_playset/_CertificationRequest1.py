# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CertificationRequest2
from . import Max140Text

class CertificationRequest1(base_types._BaseFieldType):

	__slots__ = ["_CertReqInf", "_KeyId", "_KeyVrsn"]
	@property
	def CertReqInf(self):
		return self._CertReqInf

	@CertReqInf.setter
	def CertReqInf(self, value):
		self._CertReqInf = value if value is not None else base_types.UninitialisedField(self, 'CertReqInf', CertificationRequest2, False)

	@CertReqInf.deleter
	def CertReqInf(self):
		del self._CertReqInf
		self._CertReqInf = base_types.UninitialisedField(self, 'CertReqInf', CertificationRequest2, False)

	@property
	def KeyId(self):
		return self._KeyId

	@KeyId.setter
	def KeyId(self, value):
		self._KeyId = value if value is not None else base_types.UninitialisedField(self, 'KeyId', Max140Text, False)

	@KeyId.deleter
	def KeyId(self):
		del self._KeyId
		self._KeyId = base_types.UninitialisedField(self, 'KeyId', Max140Text, False)

	@property
	def KeyVrsn(self):
		return self._KeyVrsn

	@KeyVrsn.setter
	def KeyVrsn(self, value):
		self._KeyVrsn = value if value is not None else base_types.UninitialisedField(self, 'KeyVrsn', Max140Text, False)

	@KeyVrsn.deleter
	def KeyVrsn(self):
		del self._KeyVrsn
		self._KeyVrsn = base_types.UninitialisedField(self, 'KeyVrsn', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertReqInf', type=CertificationRequest2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyVrsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))