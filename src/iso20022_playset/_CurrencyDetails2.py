# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import Exact3NumericText
from . import Max35Text
from . import Number

class CurrencyDetails2(base_types._BaseFieldType):

	__slots__ = ["_AlphaCd", "_Dcml", "_Nm", "_NmrcCd"]
	@property
	def AlphaCd(self):
		return self._AlphaCd

	@AlphaCd.setter
	def AlphaCd(self, value):
		self._AlphaCd = value if value is not None else base_types.UninitialisedField(self, 'AlphaCd', ActiveCurrencyCode, False)

	@AlphaCd.deleter
	def AlphaCd(self):
		del self._AlphaCd
		self._AlphaCd = base_types.UninitialisedField(self, 'AlphaCd', ActiveCurrencyCode, False)

	@property
	def Dcml(self):
		return self._Dcml

	@Dcml.setter
	def Dcml(self, value):
		self._Dcml = value if value is not None else base_types.UninitialisedField(self, 'Dcml', Number, False)

	@Dcml.deleter
	def Dcml(self):
		del self._Dcml
		self._Dcml = base_types.UninitialisedField(self, 'Dcml', Number, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@property
	def NmrcCd(self):
		return self._NmrcCd

	@NmrcCd.setter
	def NmrcCd(self, value):
		self._NmrcCd = value if value is not None else base_types.UninitialisedField(self, 'NmrcCd', Exact3NumericText, False)

	@NmrcCd.deleter
	def NmrcCd(self):
		del self._NmrcCd
		self._NmrcCd = base_types.UninitialisedField(self, 'NmrcCd', Exact3NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AlphaCd', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dcml', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmrcCd', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
	))