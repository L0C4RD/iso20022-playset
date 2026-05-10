import base_types
import ActiveCurrencyCode
import ISODate
import AgreementFramework1Choice
import Max140Text

class Agreement4(base_types._BaseFieldType):

	__slots__ = ["_AgrmtFrmwk", "_AgrmtDtls", "_AgrmtDt", "_BaseCcy", "_AgrmtId"]
	@property
	def AgrmtFrmwk(self):
		return self._AgrmtFrmwk

	@AgrmtFrmwk.setter
	def AgrmtFrmwk(self, value):
		self._AgrmtFrmwk = value if type(value) != auto else self.make_default("AgrmtFrmwk")

	@AgrmtFrmwk.deleter
	def AgrmtFrmwk(self):
		del self._AgrmtFrmwk
		self._AgrmtFrmwk = None

	@property
	def AgrmtDtls(self):
		return self._AgrmtDtls

	@AgrmtDtls.setter
	def AgrmtDtls(self, value):
		self._AgrmtDtls = value if type(value) != auto else self.make_default("AgrmtDtls")

	@AgrmtDtls.deleter
	def AgrmtDtls(self):
		del self._AgrmtDtls
		self._AgrmtDtls = None

	@property
	def AgrmtDt(self):
		return self._AgrmtDt

	@AgrmtDt.setter
	def AgrmtDt(self, value):
		self._AgrmtDt = value if type(value) != auto else self.make_default("AgrmtDt")

	@AgrmtDt.deleter
	def AgrmtDt(self):
		del self._AgrmtDt
		self._AgrmtDt = None

	@property
	def BaseCcy(self):
		return self._BaseCcy

	@BaseCcy.setter
	def BaseCcy(self, value):
		self._BaseCcy = value if type(value) != auto else self.make_default("BaseCcy")

	@BaseCcy.deleter
	def BaseCcy(self):
		del self._BaseCcy
		self._BaseCcy = None

	@property
	def AgrmtId(self):
		return self._AgrmtId

	@AgrmtId.setter
	def AgrmtId(self, value):
		self._AgrmtId = value if type(value) != auto else self.make_default("AgrmtId")

	@AgrmtId.deleter
	def AgrmtId(self):
		del self._AgrmtId
		self._AgrmtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrmtFrmwk', type=AgreementFramework1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrmtDtls', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrmtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BaseCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrmtId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

