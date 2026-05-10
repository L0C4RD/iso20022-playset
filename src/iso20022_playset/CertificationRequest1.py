import base_types
import CertificationRequest2
import Max140Text

class CertificationRequest1(base_types._BaseFieldType):

	__slots__ = ["_KeyId", "_CertReqInf", "_KeyVrsn"]
	@property
	def KeyId(self):
		return self._KeyId

	@KeyId.setter
	def KeyId(self, value):
		self._KeyId = value if type(value) != auto else self.make_default("KeyId")

	@KeyId.deleter
	def KeyId(self):
		del self._KeyId
		self._KeyId = None

	@property
	def CertReqInf(self):
		return self._CertReqInf

	@CertReqInf.setter
	def CertReqInf(self, value):
		self._CertReqInf = value if type(value) != auto else self.make_default("CertReqInf")

	@CertReqInf.deleter
	def CertReqInf(self):
		del self._CertReqInf
		self._CertReqInf = None

	@property
	def KeyVrsn(self):
		return self._KeyVrsn

	@KeyVrsn.setter
	def KeyVrsn(self, value):
		self._KeyVrsn = value if type(value) != auto else self.make_default("KeyVrsn")

	@KeyVrsn.deleter
	def KeyVrsn(self):
		del self._KeyVrsn
		self._KeyVrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='KeyId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertReqInf', type=CertificationRequest2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyVrsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

