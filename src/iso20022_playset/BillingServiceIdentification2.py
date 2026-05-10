import base_types
import Max35Text
import Max70Text
import BillingSubServiceIdentification1

class BillingServiceIdentification2(base_types._BaseFieldType):

	__slots__ = ["_Id", "_SubSvc", "_Desc"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def SubSvc(self):
		return self._SubSvc

	@SubSvc.setter
	def SubSvc(self, value):
		self._SubSvc = value if type(value) != auto else self.make_default("SubSvc")

	@SubSvc.deleter
	def SubSvc(self):
		del self._SubSvc
		self._SubSvc = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubSvc', type=BillingSubServiceIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
	))

