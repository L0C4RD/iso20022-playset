from . import base_types
from .DecimalNumber import DecimalNumber
from .Max4AlphaNumericText import Max4AlphaNumericText
from .Max15AlphaNumericText import Max15AlphaNumericText

class CorporateActionSD26(base_types._BaseFieldType):

	__slots__ = ["_CertClldAmt", "_CertPrfx", "_CertNb"]
	@property
	def CertClldAmt(self):
		return self._CertClldAmt

	@CertClldAmt.setter
	def CertClldAmt(self, value):
		self._CertClldAmt = value if type(value) != base_types.auto else self.make_default("CertClldAmt")

	@CertClldAmt.deleter
	def CertClldAmt(self):
		del self._CertClldAmt
		self._CertClldAmt = None

	@property
	def CertPrfx(self):
		return self._CertPrfx

	@CertPrfx.setter
	def CertPrfx(self, value):
		self._CertPrfx = value if type(value) != base_types.auto else self.make_default("CertPrfx")

	@CertPrfx.deleter
	def CertPrfx(self):
		del self._CertPrfx
		self._CertPrfx = None

	@property
	def CertNb(self):
		return self._CertNb

	@CertNb.setter
	def CertNb(self, value):
		self._CertNb = value if type(value) != base_types.auto else self.make_default("CertNb")

	@CertNb.deleter
	def CertNb(self):
		del self._CertNb
		self._CertNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertClldAmt', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertPrfx', type=Max4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertNb', type=Max15AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
	))

