# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import AgreementFramework1Choice
from . import ISODate
from . import Max140Text

class Agreement4(base_types._BaseFieldType):

	__slots__ = ["_AgrmtDt", "_AgrmtDtls", "_AgrmtFrmwk", "_AgrmtId", "_BaseCcy"]
	@property
	def AgrmtDt(self):
		return self._AgrmtDt

	@AgrmtDt.setter
	def AgrmtDt(self, value):
		self._AgrmtDt = value if value is not None else base_types.UninitialisedField(self, 'AgrmtDt', ISODate, False)

	@AgrmtDt.deleter
	def AgrmtDt(self):
		del self._AgrmtDt
		self._AgrmtDt = base_types.UninitialisedField(self, 'AgrmtDt', ISODate, False)

	@property
	def AgrmtDtls(self):
		return self._AgrmtDtls

	@AgrmtDtls.setter
	def AgrmtDtls(self, value):
		self._AgrmtDtls = value if value is not None else base_types.UninitialisedField(self, 'AgrmtDtls', Max140Text, False)

	@AgrmtDtls.deleter
	def AgrmtDtls(self):
		del self._AgrmtDtls
		self._AgrmtDtls = base_types.UninitialisedField(self, 'AgrmtDtls', Max140Text, False)

	@property
	def AgrmtFrmwk(self):
		return self._AgrmtFrmwk

	@AgrmtFrmwk.setter
	def AgrmtFrmwk(self, value):
		self._AgrmtFrmwk = value if value is not None else base_types.UninitialisedField(self, 'AgrmtFrmwk', AgreementFramework1Choice, False)

	@AgrmtFrmwk.deleter
	def AgrmtFrmwk(self):
		del self._AgrmtFrmwk
		self._AgrmtFrmwk = base_types.UninitialisedField(self, 'AgrmtFrmwk', AgreementFramework1Choice, False)

	@property
	def AgrmtId(self):
		return self._AgrmtId

	@AgrmtId.setter
	def AgrmtId(self, value):
		self._AgrmtId = value if value is not None else base_types.UninitialisedField(self, 'AgrmtId', Max140Text, False)

	@AgrmtId.deleter
	def AgrmtId(self):
		del self._AgrmtId
		self._AgrmtId = base_types.UninitialisedField(self, 'AgrmtId', Max140Text, False)

	@property
	def BaseCcy(self):
		return self._BaseCcy

	@BaseCcy.setter
	def BaseCcy(self, value):
		self._BaseCcy = value if value is not None else base_types.UninitialisedField(self, 'BaseCcy', ActiveCurrencyCode, False)

	@BaseCcy.deleter
	def BaseCcy(self):
		del self._BaseCcy
		self._BaseCcy = base_types.UninitialisedField(self, 'BaseCcy', ActiveCurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrmtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrmtDtls', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrmtFrmwk', type=AgreementFramework1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrmtId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BaseCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))