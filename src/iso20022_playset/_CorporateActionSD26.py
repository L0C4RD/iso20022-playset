# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import Max15AlphaNumericText
from . import Max4AlphaNumericText

class CorporateActionSD26(base_types._BaseFieldType):

	__slots__ = ["_CertClldAmt", "_CertNb", "_CertPrfx"]
	@property
	def CertClldAmt(self):
		return self._CertClldAmt

	@CertClldAmt.setter
	def CertClldAmt(self, value):
		self._CertClldAmt = value if value is not None else base_types.UninitialisedField(self, 'CertClldAmt', DecimalNumber, False)

	@CertClldAmt.deleter
	def CertClldAmt(self):
		del self._CertClldAmt
		self._CertClldAmt = base_types.UninitialisedField(self, 'CertClldAmt', DecimalNumber, False)

	@property
	def CertNb(self):
		return self._CertNb

	@CertNb.setter
	def CertNb(self, value):
		self._CertNb = value if value is not None else base_types.UninitialisedField(self, 'CertNb', Max15AlphaNumericText, False)

	@CertNb.deleter
	def CertNb(self):
		del self._CertNb
		self._CertNb = base_types.UninitialisedField(self, 'CertNb', Max15AlphaNumericText, False)

	@property
	def CertPrfx(self):
		return self._CertPrfx

	@CertPrfx.setter
	def CertPrfx(self, value):
		self._CertPrfx = value if value is not None else base_types.UninitialisedField(self, 'CertPrfx', Max4AlphaNumericText, False)

	@CertPrfx.deleter
	def CertPrfx(self):
		del self._CertPrfx
		self._CertPrfx = base_types.UninitialisedField(self, 'CertPrfx', Max4AlphaNumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertClldAmt', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertNb', type=Max15AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertPrfx', type=Max4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))